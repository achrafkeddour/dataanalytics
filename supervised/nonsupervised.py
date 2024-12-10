import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Générer des données fictives pour le clustering
# Chaque point représente un client avec deux caractéristiques : 
# - Dépenses mensuelles (en €)
# - Niveau de satisfaction (sur 10)
data = {
    'depenses': [200, 400, 600, 800, 1000, 1500, 1700, 2000, 2200, 2500],
    'satisfaction': [2, 3, 5, 6, 7, 8, 6, 9, 10, 7]
}
df = pd.DataFrame(data)

# Préparer les données pour K-Means
X = df[['depenses', 'satisfaction']].values

# Appliquer l'algorithme K-Means (choisir 3 clusters)
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X)

# Récupérer les étiquettes de clusters
df['cluster'] = kmeans.labels_

# Visualiser les clusters
plt.figure(figsize=(8, 6))
colors = ['red', 'blue', 'green']
for cluster in range(3):
    cluster_data = df[df['cluster'] == cluster]
    plt.scatter(cluster_data['depenses'], cluster_data['satisfaction'],
                color=colors[cluster], label=f'Cluster {cluster + 1}')

# Ajouter les centres des clusters
centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], color='yellow', marker='X', s=200, label='Centres des clusters')

# Étiquettes et légende
plt.title('Clustering des clients : Dépenses vs Satisfaction')
plt.xlabel('Dépenses mensuelles (en €)')
plt.ylabel('Niveau de satisfaction (sur 10)')
plt.legend()
plt.grid(True)

# Afficher le graphique
plt.show()
