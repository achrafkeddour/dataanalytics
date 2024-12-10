# Importer les bibliothèques
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Lire les données depuis un fichier CSV
data = pd.read_csv('data.csv') 
# Extraire les colonnes "publicite" (budget) et "ventes"
X = data['publicite'].values.reshape(-1, 1)  # Budget publicitaire (en milliers d'euros)
y = data['ventes'].values  # Nombre de ventes

# Créer et entraîner le modèle
model = LinearRegression()
model.fit(X, y)

# Afficher l'équation : Y = aX + b
a = model.coef_[0]  # pente
b = model.intercept_  # ordonnée à l'origine
print(f"Équation : Ventes = {a:.2f} * Budget + {b:.2f}")

# Nouvelles données pour prédiction (budget publicitaire en milliers d'euros)
nouveaux_budgets = np.array([[3], [7], [8]])  # Exemple : budgets à tester

# Faire des prédictions
ventes_predites = model.predict(nouveaux_budgets)

# Afficher les résultats
print("Budgets publicitaires (en milliers d'euros) :", nouveaux_budgets.flatten())
print("Ventes prédites :", np.round(ventes_predites, 2))

# Tracer le graphique
plt.scatter(X, y, color='blue', label='Données existantes')  # points d'origine
plt.plot(X, model.predict(X), color='red', label='Ligne de régression')  # ligne résultante
plt.scatter(nouveaux_budgets, ventes_predites, color='green', label='Prédictions', marker='x', s=100)  # nouveaux points

# Étiquettes des axes et titre
plt.xlabel('Budget publicitaire (en milliers d\'euros)')
plt.ylabel('Nombre de ventes')
plt.title('Prédiction des ventes en fonction du budget publicitaire')
plt.legend()

# Afficher le graphique
plt.show()
