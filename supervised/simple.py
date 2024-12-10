from sklearn.linear_model import LinearRegression

# Exemple simple de données
X = [[1], [2], [3], [4], [5]]  # Les valeurs des caractéristiques (entrée)
y = [2, 4, 6, 8, 10]          # Les valeurs cibles (sortie)

# Créer et entraîner le modèle
model = LinearRegression()
model.fit(X, y)

# Faire des prédictions
nouveau_X = [[6], [7], [8]]  # Nouvelles données pour prédire
predits = model.predict(nouveau_X)

print("Prédictions :", predits)