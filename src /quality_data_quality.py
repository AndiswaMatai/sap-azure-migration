from pyspark.sql.functions import col

def run_dq_checks(df):

    print("\n[DQ] Running Data Quality Checks...\n")

    # Null check summary
    null_counts = {
        c: df.filter(col(c).isNull()).count()
        for c in df.columns
    }

    print("[DQ] Null Values Per Column:")
    print(null_counts)

    # Duplicate check
    dup_count = df.count() - df.dropDuplicates().count()

    print(f"[DQ] Duplicate Records: {dup_count}")

    return {
        "nulls": null_counts,
        "duplicates": dup_count
    }
