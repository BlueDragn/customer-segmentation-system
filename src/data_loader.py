import pandas as pd

def load_data(file_path):

    df = pd.read_csv(file_path)

    print("Dataset loaded successfully.")
    print(f"shape: {df.shape}")
    print(f"columns: {df.columns}")
    return df