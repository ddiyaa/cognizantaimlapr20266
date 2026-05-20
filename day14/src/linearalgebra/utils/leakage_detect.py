import pandas as pd
import numpy as np
from linearalgebra.configurations.conf import Config
def leakage_detection(df, target_col):
    df.columns = df.columns.str.strip()

    print("Available columns:")
    print(df.columns.tolist())

    if target_col not in df.columns:
        print(f"ERROR: '{target_col}' column not found")
        return

    # Convert True/False target to 1/0
    df[target_col] = df[target_col].map({
        True: 1,
        False: 0,
        "True": 1,
        "False": 0,
        "TRUE": 1,
        "FALSE": 0
    })

    print("=" * 50)
    print("1. High Correlation Check")
    print("=" * 50)

    numeric_df = df.select_dtypes(include=[np.number])

    print("Numeric columns:")
    print(numeric_df.columns.tolist())

    corr = numeric_df.corr()[target_col].sort_values(ascending=False)
    print(corr)

    print("\nPotential leakage columns:")
    print(corr[(corr.abs() > 0.90) & (corr.index != target_col)])

if __name__ == "__main__":
    df = pd.read_csv(Config.customer_data_path)
    # remove leading/trailing spaces
    df.columns = df.columns.str.strip()


    leakage_detection(df, "churned")