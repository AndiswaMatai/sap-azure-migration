from bronze.bronze_loader import load_bronze
from silver.patient_transform import transform_silver
from gold.patient_analytics import build_gold
from quality.data_quality import run_dq_checks
from reconciliation.migration_validation import reconcile

def run_pipeline():

    print("\n🚀 STARTING SPARK HEALTHCARE MIGRATION PIPELINE\n")

    # BRONZE
    bronze_df = load_bronze("data/raw/patients.csv")

    # SILVER
    silver_df = transform_silver(bronze_df)

    # DQ CHECKS
    dq_results = run_dq_checks(silver_df)

    # GOLD
    gold_df = build_gold(silver_df)

    # RECONCILIATION (simulate migration validation)
    recon = reconcile(silver_df, silver_df)

    print("\n✅ PIPELINE COMPLETED SUCCESSFULLY")

if __name__ == "__main__":
    run_pipeline()
