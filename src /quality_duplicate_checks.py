def check_duplicates(df, key_column: str):
    duplicates = df[df.duplicated(subset=[key_column])]

    print(f"[DQ] Duplicate records found: {len(duplicates)}")

    return duplicates
