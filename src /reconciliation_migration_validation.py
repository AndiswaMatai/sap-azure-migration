def reconcile(source_df, target_df):
    """
    Simulates reconciliation between SAP (source) and Azure (target)
    """

    source_keys = source_df.select("patient_id").distinct()
    target_keys = target_df.select("patient_id").distinct()

    missing_in_target = source_keys.subtract(target_keys)
    new_in_target = target_keys.subtract(source_keys)

    print(f"[RECON] Missing in Target: {missing_in_target.count()}")
    print(f"[RECON] New in Target: {new_in_target.count()}")

    return {
        "missing_in_target": missing_in_target,
        "new_in_target": new_in_target
    }
