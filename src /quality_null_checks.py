def check_nulls(df):
    null_summary = df.isnull().sum()

    print("[DQ] Null value summary:")
    print(null_summary)

    return null_summary
