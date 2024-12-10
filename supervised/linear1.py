import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Lire les données depuis un fichier CSV
data = pd.read_csv('vaccination.csv')

# Extraire les colonnes "budget_vaccination" et "nombre_vaccines"
X = data['budget_vaccination'].values.reshape(-1, 1)  # Budget de vaccination (en milliers d'euros)
y = data['nombre_vaccines'].values  # Nombre de personnes vaccinées

# Créer et entraîner le modèle
model = LinearRegression()
model.fit(X, y)

# Afficher l'équation : Y = aX + b
a = model.coef_[0]  # pente
b = model.intercept_  # ordonnée à l'origine
print(f"Équation : Nombre de personnes vaccinées = {a:.2f} * Budget de vaccination + {b:.2f}")

# Nouvelles données pour prédiction (budget de vaccination en milliers d'euros)
nouveaux_budgets = np.array([[3], [7], [8]])  # Exemple : budgets à tester

# Faire des prédictions
vaccines_predits = model.predict(nouveaux_budgets)

# Afficher les résultats
print("Budgets de vaccination (en milliers d'euros) :", nouveaux_budgets.flatten())
print("Nombre de personnes vaccinées prédites :", np.round(vaccines_predits, 2))

# Tracer le graphique
plt.scatter(X, y, color='blue', label='Données existantes')  # points d'origine
plt.plot(X, model.predict(X), color='red', label='Ligne de régression')  # ligne résultante
plt.scatter(nouveaux_budgets, vaccines_predits, color='green', label='Prédictions', marker='x', s=100)  # nouveaux points

# Étiquettes des axes et titre
plt.xlabel('Budget de vaccination (en milliers d\'euros)')
plt.ylabel('Nombre de personnes vaccinées')
plt.title('Prédiction du nombre de personnes vaccinées en fonction du budget de vaccination')
plt.legend()

# Afficher le graphique
plt.show()
