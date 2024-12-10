# Importation des bibliothèques
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Données spécifiques (exemple de coordonnées en 2D)
data = np.array([
    [2.1, 3.2], [1.5, 2.8], [3.0, 3.0], [5.0, 8.0],
    [8.0, 8.0], [1.0, 0.6], [9.0, 11.0], [8.5, 10.0],
    [2.0, 1.0], [7.5, 8.0], [2.2, 2.5], [8.1, 9.0],
])

# Visualisation des données initiales
plt.scatter(data[:, 0], data[:, 1], s=50, color='blue')
plt.title("Données avant clustering")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

# Création et entraînement du modèle K-Means
kmeans = KMeans(n_clusters=3, random_state=0)  # On choisit 3 clusters
kmeans.fit(data)

# Prédiction des clusters
labels = kmeans.predict(data)
centers = kmeans.cluster_centers_  # Centres des clusters

# Visualisation des résultats
plt.scatter(data[:, 0], data[:, 1], c=labels, s=50, cmap='viridis')  # Points colorés selon les clusters
plt.scatter(centers[:, 0], centers[:, 1], c='red', s=200, marker='x')  # Centres des clusters
plt.title("Clustering K-Means avec des données précises")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()