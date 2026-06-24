from pyspark.sql.functions import count, when, col

def build_gold(df):
    """
    Gold layer:
    Aggregated healthcare metrics
    """

    result = df.groupBy().agg(
        count("*").alias("total_patients"),
        count("patient_id").alias("patient_records"),
        count(when(col("gender") == "MALE", True)).alias("male_patients"),
        count(when(col("gender") == "FEMALE", True)).alias("female_patients")
    )

    result.show()

    return result
