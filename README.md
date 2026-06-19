# SAP ECC → Azure Migration Pipeline

A production-style data migration pipeline that extracts SAP ECC flat-file exports (GL accounts, vendors, purchase orders, journal entries), validates them against migration rules, and loads them into Azure-ready conformed tables — the pattern used when moving an ERP from on-premise SAP to Azure SQL / Synapse Analytics.

## Why this exists

SAP migrations are high-stakes: a single bad record (deleted PO, duplicate vendor, zero-value entry) can break downstream financial reporting. This project demonstrates the three-phase approach that makes migrations safe: extract → validate → transform, with every rejected record logged for sign-off before go-live.

## SAP Tables Modelled

| SAP Table | Description | Azure Target |
|---|---|---|
| SKA1 | GL Account master | `az_gl_accounts` |
| LFA1 | Vendor master | `az_vendors` |
| EKKO/EKPO | Purchase order header/line | `az_purchase_orders` |
| BSEG | Accounting document line items | `az_journal_entries` |

## Architecture

```
SAP ECC extract (flat CSV)
        │
        ▼
[Phase 1: Extract]  generate_sample_data.py  →  data/raw/*.csv
        │
        ▼
[Phase 2: Validate]  run_migration.py
   • Deleted records (LOEKZ = L)
   • Duplicate keys
   • Zero/negative values
   • Missing mandatory fields
        │
        ├── REJECTED ──▶ migration_validation_log (ERROR / WARNING)
        │
        ▼
[Phase 3: Transform & Load]
   • SAP field names → business-friendly Azure column names
   • SAP date format (YYYYMMDD) → ISO 8601
   • Debit/Credit (S/H) → signed amounts
        │
        ▼
   az_gl_accounts / az_vendors / az_purchase_orders / az_journal_entries
```

## Sample Migration Run

```
Entity               Source  Passed  Migrated  Rejected
-------------------------------------------------------
GL Accounts              40      40        40         0
Vendors                  10      10        10         0
Purchase Orders         120     118       118         2
Journal Entries         300     300       300         0

VALIDATION LOG: WARNING: 2 (deleted POs excluded)
```

## Tech stack

Python, SQLite (→ Azure SQL / Synapse in production), standard library only.

## Running it

```bash
python src/generate_sample_data.py
python src/run_migration.py
```

Run the tests:

```bash
python -m unittest discover -s tests -v
```

## What I'd add for production

- Replace flat-file extracts with SAP RFC/BAPI calls using `pyrfc` for live extraction
- Add delta extraction logic (capture only records changed since last run using CDHDR change documents)
- Load into Azure Data Factory with Synapse Analytics as the target
- Build a migration dashboard in Power BI showing entity-by-entity progress, rejection rates, and validation trends

## License

MIT
