def analyze_clusters(df):

    cluster_summary = df.groupby('Cluster').agg({
        "Age": "mean",
        "Annual Income (k$)": "mean",
        "Spending Score (1-100)": "mean",

    })

    cluster_summary["Customer_Count"] = (
        df.groupby("Cluster").size()
    )

    return cluster_summary