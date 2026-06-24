from ingestion.extract_sap import extract_sap_data
from bronze.bronze_loader import load_to_bronze
from silver.patient_transform import transform_patients
from gold.patient_analytics import generate_patient_metrics
from quality.null_checks import check_nulls
from quality.duplicate_checks import check_duplicates

def run_pipeline():
    print("\n🚀 STARTING HEALTHCARE MIGRATION PIPELINE\n")

    # 1. INGESTION
    df_raw = extract_sap_data("data/raw/patients.csv")

    # 2. BRONZE
    load_to_bronze(df_raw, "data/bronze/patients_bronze.csv")

    # 3. SILVER
    df_silver = transform_patients(df_raw)

    # 4. QUALITY CHECKS
    check_nulls(df_silver)
    check_duplicates(df_silver, "patient_id")

    # 5. GOLD
    df_gold = generate_patient_metrics(df_silver)

    print("\n📊 GOLD OUTPUT")
    print(df_gold)

    print("\n✅ PIPELINE COMPLETED SUCCESSFULLY")

if __name__ == "__main__":
    run_pipeline()
