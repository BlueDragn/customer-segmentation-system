import pandas as pd

def preprocess_data(df):
    print("\n=== Dataset Information ===")

    print(f"Shape: {df.shape}")
    # Missing Values
    print("\nMissing Values:")
    print(df.isnull().sum())

    # Duplicate Rows
    print("\nDuplicate Rows:")
    duplicate_rows = df.duplicated().sum()
    print(f"Number of duplicate rows: {duplicate_rows}")

    # Remove CustomerID
    df = df.drop(columns=["CustomerID"])
    print("\nCustomerID column removed.")

    return df
