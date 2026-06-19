"""Run with: python -m unittest discover -s tests -v"""
import sqlite3
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))
from run_migration import validate_purchase_orders, validate_vendors, _sap_date, get_conn, migrate_gl_accounts


def _mem_conn():
    conn = sqlite3.connect(":memory:")
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS migration_validation_log (
            entity TEXT, record_id TEXT, issue TEXT, severity TEXT, logged_ts TEXT);
    """)
    return conn


class TestValidation(unittest.TestCase):
    def test_deleted_po_rejected(self):
        records = [{"EBELN": "PO1", "LOEKZ": "L", "NETWR": "1000.00"}]
        conn = _mem_conn()
        valid, issues = validate_purchase_orders(records, conn)
        self.assertEqual(len(valid), 0)
        self.assertEqual(issues, 1)

    def test_clean_po_passes(self):
        records = [{"EBELN": "PO2", "LOEKZ": "", "NETWR": "5000.00"}]
        conn = _mem_conn()
        valid, issues = validate_purchase_orders(records, conn)
        self.assertEqual(len(valid), 1)
        self.assertEqual(issues, 0)

    def test_duplicate_vendor_rejected(self):
        records = [
            {"LIFNR": "V001", "NAME1": "Vendor A"},
            {"LIFNR": "V001", "NAME1": "Vendor A Duplicate"},
        ]
        conn = _mem_conn()
        valid, issues = validate_vendors(records, conn)
        self.assertEqual(len(valid), 1)
        self.assertEqual(issues, 1)

    def test_zero_value_po_rejected(self):
        records = [{"EBELN": "PO3", "LOEKZ": "", "NETWR": "0.00"}]
        conn = _mem_conn()
        valid, issues = validate_purchase_orders(records, conn)
        self.assertEqual(len(valid), 0)


class TestTransform(unittest.TestCase):
    def test_sap_date_converts(self):
        self.assertEqual(_sap_date("20250101"), "2025-01-01")

    def test_sap_date_invalid_returns_none(self):
        self.assertIsNone(_sap_date("not-a-date"))


if __name__ == "__main__":
    unittest.main()
