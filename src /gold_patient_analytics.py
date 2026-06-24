import pandas as pd

def generate_patient_metrics(df: pd.DataFrame) -> pd.DataFrame:
    """
    Gold layer:
    Business-ready aggregated dataset
    """

    metrics = {
        "total_patients": len(df),
        "unique_patients": df["patient_id"].nunique() if "patient_id" in df else 0,
        "male_patients": len(df[df["gender"] == "MALE"]) if "gender" in df else 0,
        "female_patients": len(df[df["gender"] == "FEMALE"]) if "gender" in df else 0
    }

    return pd.DataFrame([metrics])
