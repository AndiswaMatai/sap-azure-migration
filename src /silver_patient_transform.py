import pandas as pd

def transform_patients(df: pd.DataFrame) -> pd.DataFrame:
    """
    Silver layer:
    - Removes duplicates
    - Handles nulls
    - Standardises formats
    """

    initial_count = len(df)

    # Remove duplicates
    df = df.drop_duplicates()

    # Fill missing values
    df = df.fillna({
        "patient_id": "UNKNOWN",
        "name": "UNKNOWN",
        "gender": "UNKNOWN"
    })

    # Standardise text fields
    if "gender" in df.columns:
        df["gender"] = df["gender"].str.upper()

    print(f"[SILVER] Cleaned records: {initial_count} → {len(df)}")

    return df
