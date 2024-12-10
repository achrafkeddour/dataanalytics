from sklearn.cluster import KMeans

# Exemple simple de données (points dans un espace 2D)
X = [[1, 2], [2, 3], [3, 4], [8, 8], [9, 9], [10, 10]]  # Les valeurs des caractéristiques

# Créer et entraîner le modèle
kmeans = KMeans(n_clusters=2, random_state=0)  # 2 clusters
kmeans.fit(X)

# Faire des prédictions
nouveau_X = [[4, 5], [8, 7]]  # Nouvelles données pour attribuer un cluster
predits = kmeans.predict(nouveau_X)

print("Clusters pour les nouvelles données :", predits)
print("Centres des clusters :", kmeans.cluster_centers_)