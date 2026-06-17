
from data_loader import load_data
from preprocessor import preprocess_data




def main():
    df = load_data("data/raw/Mall_Customers.csv")

    cleaned_df = preprocess_data(df)

    print("\nProcessed Dataset:")
    print(cleaned_df.head())


if __name__ == "__main__":
    main()