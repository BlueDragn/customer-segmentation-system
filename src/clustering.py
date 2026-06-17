from sklearn.cluster import KMeans

def create_clusters(scaled_data):

    kmeans = KMeans(
        n_clusters=5,
        random_state=42,
        n_init=10
    )
    cluster_labels = kmeans.fit_predict(scaled_data)
    return cluster_labels