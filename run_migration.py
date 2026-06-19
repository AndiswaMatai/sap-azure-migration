"""
SAP ECC -> Azure migration pipeline.

Simulates the three phases of a real SAP-to-Azure migration:
1. EXTRACT   — read SAP flat-file extracts (as produced by SE16/ABAP reports)
2. VALIDATE  — check for migration blockers (deleted records, missing refs,
               SAP-specific flags) before loading into Azure
3. TRANSFORM — rename SAP technical field names to business-friendly Azure
               column names, apply type conversions, build conformed tables

Run:
    python src/generate_sample_data.py
    python src/run_migration.py
"""
import csv
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

RAW = Path(__file__).resolve().parent.parent / "data" / "raw"
PROCESSED = Path(__file__).resolve().parent.parent / "data" / "processed"
DB_PATH = Path(__file__).resolve().parent.parent / "data" / "migration.db"
PROCESSED.mkdir(parents=True, exist_ok=True)

def now(): return datetime.now(timezone.utc).isoformat()
def load(fname): return list(csv.DictReader(open(RAW / fname)))

def get_conn():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS az_gl_accounts (
            account_id TEXT PRIMARY KEY, account_type TEXT, account_name TEXT,
            currency TEXT, is_balance_sheet INTEGER, migrated_ts TEXT);
        CREATE TABLE IF NOT EXISTS az_vendors (
            vendor_id TEXT PRIMARY KEY, vendor_name TEXT, country TEXT,
            city TEXT, tax_number TEXT, migrated_ts TEXT);
        CREATE TABLE IF NOT EXISTS az_purchase_orders (
            po_number TEXT PRIMARY KEY, vendor_id TEXT, po_date TEXT,
            currency TEXT, net_value REAL, company_code TEXT,
            purchasing_group TEXT, migrated_ts TEXT);
        CREATE TABLE IF NOT EXISTS az_journal_entries (
            document_number TEXT, line_item TEXT, account_id TEXT,
            amount REAL, debit_credit TEXT, posting_date TEXT,
            document_date TEXT, description TEXT, migrated_ts TEXT,
            PRIMARY KEY (document_number, line_item));
        CREATE TABLE IF NOT EXISTS migration_validation_log (
            entity TEXT, record_id TEXT, issue TEXT, severity TEXT, logged_ts TEXT);
        CREATE TABLE IF NOT EXISTS migration_summary (
            entity TEXT, total_source INT, passed_validation INT,
            migrated INT, rejected INT, run_ts TEXT);
    """)
    return conn


# ── PHASE 1: VALIDATE ────────────────────────────────────────────────────────
def validate_gl_accounts(records, conn):
    valid, issues = [], 0
    for r in records:
        if not r["SAKNR"] or not r["TXT50"]:
            conn.execute("INSERT INTO migration_validation_log VALUES (?,?,?,?,?)",
                ("GL_ACCOUNT", r.get("SAKNR","?"), "Missing account number or description", "ERROR", now()))
            issues += 1; continue
        valid.append(r)
    return valid, issues

def validate_vendors(records, conn):
    valid, issues = [], 0
    seen = set()
    for r in records:
        if r["LIFNR"] in seen:
            conn.execute("INSERT INTO migration_validation_log VALUES (?,?,?,?,?)",
                ("VENDOR", r["LIFNR"], "Duplicate vendor ID", "ERROR", now()))
            issues += 1; continue
        seen.add(r["LIFNR"])
        valid.append(r)
    return valid, issues

def validate_purchase_orders(records, conn):
    valid, issues = [], 0
    for r in records:
        if r.get("LOEKZ") == "L":
            conn.execute("INSERT INTO migration_validation_log VALUES (?,?,?,?,?)",
                ("PURCHASE_ORDER", r["EBELN"], "Deleted PO excluded from migration", "WARNING", now()))
            issues += 1; continue
        if float(r["NETWR"]) <= 0:
            conn.execute("INSERT INTO migration_validation_log VALUES (?,?,?,?,?)",
                ("PURCHASE_ORDER", r["EBELN"], "Zero/negative net value", "WARNING", now()))
            issues += 1; continue
        valid.append(r)
    return valid, issues


# ── PHASE 2: TRANSFORM & LOAD ────────────────────────────────────────────────
def _sap_date(d):
    try: return datetime.strptime(d, "%Y%m%d").strftime("%Y-%m-%d")
    except: return None

def migrate_gl_accounts(records, conn):
    ts = now()
    conn.executemany("INSERT OR REPLACE INTO az_gl_accounts VALUES (?,?,?,?,?,?)",
        [(r["SAKNR"], r["KTOKS"], r["TXT50"], r["WAERS"], 1 if r["XBILK"]=="X" else 0, ts) for r in records])
    conn.commit(); return len(records)

def migrate_vendors(records, conn):
    ts = now()
    conn.executemany("INSERT OR REPLACE INTO az_vendors VALUES (?,?,?,?,?,?)",
        [(r["LIFNR"], r["NAME1"], r["LAND1"], r["ORT01"], r["STCD1"], ts) for r in records])
    conn.commit(); return len(records)

def migrate_purchase_orders(records, conn):
    ts = now()
    conn.executemany("INSERT OR REPLACE INTO az_purchase_orders VALUES (?,?,?,?,?,?,?,?)",
        [(r["EBELN"], r["LIFNR"], _sap_date(r["BEDAT"]), r["WAERS"],
          float(r["NETWR"]), r["BUKRS"], r["EKGRP"], ts) for r in records])
    conn.commit(); return len(records)

def migrate_journal_entries(records, conn):
    ts = now()
    conn.executemany("INSERT OR REPLACE INTO az_journal_entries VALUES (?,?,?,?,?,?,?,?,?)",
        [(r["BELNR"], r["BUZEI"], r["SAKNR"],
          float(r["DMBTR"]) * (1 if r["SHKZG"]=="S" else -1),
          r["SHKZG"], _sap_date(r["BUDAT"]), _sap_date(r["BLDAT"]), r["SGTXT"], ts) for r in records])
    conn.commit(); return len(records)


# ── MAIN ─────────────────────────────────────────────────────────────────────
def main():
    print("=" * 55)
    print("SAP ECC → AZURE MIGRATION PIPELINE")
    print("=" * 55)

    conn = get_conn()
    entities = [
        ("GL Accounts",      "sap_gl_accounts.csv",    validate_gl_accounts,    migrate_gl_accounts),
        ("Vendors",          "sap_vendors.csv",         validate_vendors,        migrate_vendors),
        ("Purchase Orders",  "sap_purchase_orders.csv", validate_purchase_orders,migrate_purchase_orders),
        ("Journal Entries",  "sap_bseg.csv",            lambda r,c: (r, 0),     migrate_journal_entries),
    ]

    print(f"\n{'Entity':<20} {'Source':>7} {'Passed':>7} {'Migrated':>9} {'Rejected':>9}")
    print("-" * 55)

    for label, fname, validator, migrator in entities:
        records = load(fname)
        valid, issues = validator(records, conn)
        migrated = migrator(valid, conn)
        rejected = len(records) - migrated
        conn.execute("INSERT INTO migration_summary VALUES (?,?,?,?,?,?)",
            (label, len(records), len(valid), migrated, rejected, now()))
        print(f"{label:<20} {len(records):>7} {len(valid):>7} {migrated:>9} {rejected:>9}")

    conn.commit()
    print("\n" + "=" * 55)
    print("VALIDATION LOG SUMMARY")
    print("=" * 55)
    for row in conn.execute("SELECT severity, COUNT(*) FROM migration_validation_log GROUP BY severity").fetchall():
        print(f"   {row[0]}: {row[1]}")
    print("\nMigration complete. Data is in data/migration.db")
    conn.close()

if __name__ == "__main__":
    main()
