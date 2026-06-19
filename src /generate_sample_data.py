"""
Simulates SAP ECC flat-file extracts — the format SAP produces when you
run a data migration extract via SE16 / SQVI or a custom ABAP report.
Tables modelled: SKA1 (GL accounts), LFA1 (vendors), EKKO/EKPO (purchase
orders), BSEG (accounting document line items).
"""
import csv
import random
import uuid
from datetime import datetime, timedelta
from pathlib import Path

random.seed(55)
RAW = Path(__file__).resolve().parent.parent / "data" / "raw"
RAW.mkdir(parents=True, exist_ok=True)

# GL Accounts (SKA1-style)
gl_accounts = []
ACCOUNT_TYPES = [("1", "Assets"), ("2", "Liabilities"), ("3", "Equity"), ("4", "Revenue"), ("5", "Expenses")]
for acct_type, acct_name in ACCOUNT_TYPES:
    for i in range(8):
        gl_accounts.append({
            "SAKNR": f"{acct_type}{str(i+1000).zfill(6)}",
            "KTOKS": acct_type,
            "TXT50": f"{acct_name} Account {i+1}",
            "WAERS": "ZAR",
            "XBILK": "X" if acct_type in ["1","2","3"] else "",
        })

# Vendors (LFA1-style)
vendors = []
VENDOR_NAMES = ["Sappi Ltd", "Eskom Holdings", "Transnet", "MTN Group", "Shoprite Holdings",
                "Anglo American", "Sasol Ltd", "Standard Bank", "Vodacom", "Tiger Brands"]
for i, name in enumerate(VENDOR_NAMES):
    vendors.append({
        "LIFNR": f"V{str(i+1).zfill(6)}",
        "NAME1": name,
        "LAND1": "ZA",
        "ORT01": random.choice(["Johannesburg", "Cape Town", "Durban", "Pretoria"]),
        "STCD1": f"{random.randint(1000000000, 9999999999)}",
        "KTOKK": "LIEF",
    })

# Purchase Orders (EKKO/EKPO-style)
purchase_orders = []
start = datetime(2025, 1, 1)
for i in range(120):
    po_date = start + timedelta(days=random.randint(0, 180))
    vendor = random.choice(vendors)
    net_value = round(random.uniform(5000, 500000), 2)
    purchase_orders.append({
        "EBELN": f"45{str(4500000000 + i)}",
        "LIFNR": vendor["LIFNR"],
        "BEDAT": po_date.strftime("%Y%m%d"),
        "WAERS": "ZAR",
        "NETWR": net_value,
        "BUKRS": "1000",
        "EKGRP": random.choice(["010", "020", "030"]),
        "LOEKZ": "" if random.random() > 0.05 else "L",   # L = deleted
    })

# Accounting document line items (BSEG-style)
bseg_entries = []
for i in range(300):
    doc_date = start + timedelta(days=random.randint(0, 180))
    account = random.choice(gl_accounts)
    amount = round(random.uniform(-250000, 250000), 2)
    bseg_entries.append({
        "BUKRS": "1000",
        "BELNR": f"10000{str(i).zfill(6)}",
        "GJAHR": "2025",
        "BUZEI": "001",
        "SAKNR": account["SAKNR"],
        "DMBTR": abs(amount),
        "SHKZG": "S" if amount >= 0 else "H",   # S=Debit H=Credit
        "BUDAT": doc_date.strftime("%Y%m%d"),
        "BLDAT": doc_date.strftime("%Y%m%d"),
        "SGTXT": f"Auto entry {i}",
    })

for fname, rows in [
    ("sap_gl_accounts.csv", gl_accounts),
    ("sap_vendors.csv", vendors),
    ("sap_purchase_orders.csv", purchase_orders),
    ("sap_bseg.csv", bseg_entries),
]:
    with open(RAW / fname, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=rows[0].keys())
        w.writeheader(); w.writerows(rows)

print(f"GL accounts: {len(gl_accounts)} | Vendors: {len(vendors)} | POs: {len(purchase_orders)} | BSEG entries: {len(bseg_entries)}")
