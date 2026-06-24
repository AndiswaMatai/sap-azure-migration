from pyspark.sql.functions import col, upper, when

def transform_silver(df):
    """
    Silver layer:
    - Deduplication
    - Null handling
    - Standardisation
    """

    df_clean = (
        df.dropDuplicates()
        .fillna("UNKNOWN")
    )

    if "gender" in df_clean.columns:
        df_clean = df_clean.withColumn(
            "gender",
            upper(col("gender"))
        )

    print(f"[SILVER] Records after cleaning: {df_clean.count()}")

    return df_clean
