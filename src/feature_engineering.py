import pandas as pd

def prepare_feature(df):
    df = df.copy()

    # Encode Gender
    df["Gender"] = df["Gender"].map({
        "Male": 0, "Female": 1
        })

    return df