import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt

# Charger les données
data = pd.read_csv('data.csv')  # Remplacez par le chemin vers votre fichier

# Préparer les données
features = ['Age', 'Distance_from_origin', 'Monthly_income_estimate']
scaler = StandardScaler()
data_normalized = scaler.fit_transform(data[features])

# Appliquer KMeans
kmeans = KMeans(n_clusters=3, random_state=42)
predicted_labels = kmeans.fit_predict(data_normalized)

# Visualiser les clusters
cluster_centers_original = scaler.inverse_transform(kmeans.cluster_centers_)
plt.scatter(data['Distance_from_origin'], data['Monthly_income_estimate'], c=predicted_labels, cmap='viridis', s=50)
plt.scatter(cluster_centers_original[:, 1], cluster_centers_original[:, 2], c='red', s=200, marker='x')
plt.title("KMeans Clustering (Distance vs Income)")
plt.xlabel("Distance from Origin")
plt.ylabel("Monthly Income Estimate")
plt.show()

# Score de silhouette
print(f"Silhouette Score: {silhouette_score(data_normalized, predicted_labels):.2f}")

# Ajouter les clusters au dataset
data['Cluster'] = predicted_labels
print(data)
