import pandas as pd
import os

def extract_sap_data(file_path: str) -> pd.DataFrame:
    """
    Simulates extraction from SAP ECC system.
    In real life this would be ADF / RFC / API extraction.
    """

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"SAP extract not found: {file_path}")

    df = pd.read_csv(file_path)

    # Simulate raw SAP formatting issues
    df.columns = [col.strip().lower() for col in df.columns]

    print(f"[INGESTION] Loaded {len(df)} records from SAP extract")

    return df
