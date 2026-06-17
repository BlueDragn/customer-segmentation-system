
from data_loader import load_data
from preprocessor import preprocess_data
from feature_engineering import  prepare_feature
from scaler import scale_feature
from clustering import create_clusters

def main():
    # Load the dataset
    df = load_data("data/raw/Mall_Customers.csv")

    # Preprocess the dataset
    cleaned_df = preprocess_data(df)

    print("\nProcessed Dataset:")
    print(cleaned_df.head())

    # feature engineering
    feature_df = prepare_feature(cleaned_df)

    # Scale the features
    scaled_data = scale_feature(feature_df)

    print("\nScaled Dataset Shape:")
    print(scaled_data.shape)

    # Create clusters
    cluster_labels = create_clusters(scaled_data)

    print("\nCluster Labels:")
    print(cluster_labels[:10])  # Display first 10 cluster labels

    feature_df['Cluster'] = cluster_labels
    print(feature_df.head())


if __name__ == "__main__":
    main()