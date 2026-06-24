from common.spark_session import get_spark

def load_bronze(file_path: str):
    spark = get_spark()

    df = (
        spark.read
        .option("header", True)
        .csv(file_path)
    )

    # Normalize column names (SAP-style inconsistency handling)
    df = df.toDF(*[c.strip().lower() for c in df.columns])

    print(f"[BRONZE] Loaded {df.count()} records")

    return df
