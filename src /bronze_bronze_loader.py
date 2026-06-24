import os
import pandas as pd

def load_to_bronze(df: pd.DataFrame, output_path: str):
    """
    Bronze layer = raw persisted data (no transformations)
    """

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    df.to_csv(output_path, index=False)

    print(f"[BRONZE] Data written to bronze layer: {output_path}")

    return df
