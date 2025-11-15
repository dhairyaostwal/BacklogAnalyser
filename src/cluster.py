from sklearn.cluster import KMeans

def cluster_embeddings(embeddings, n_clusters=5):
    km = KMeans(n_clusters=n_clusters, random_state=42)
    labels = km.fit_predict(embeddings)
    return labels
