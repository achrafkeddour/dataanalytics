import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

# Charger les données
df = pd.read_csv("data2.csv")
df['Date'] = pd.to_datetime(df['Date'])
df['Day'] = (df['Date'] - df['Date'].min()).dt.days  # Transformer les dates en jours

# Modèle linéaire
X = df[['Day']]
y = df['Sales']
model = LinearRegression()
model.fit(X, y)

# Prédictions
future_days = np.arange(df['Day'].max() + 1, df['Day'].max() + 8).reshape(-1, 1)
forecast = model.predict(future_days)

# Visualisation
plt.figure(figsize=(10, 5))
plt.plot(df['Date'], df['Sales'], label='Ventes historiques', marker='o')
plt.plot(pd.date_range(start=df['Date'].max() + pd.Timedelta(days=1), periods=7),
         forecast, label='Prévisions', linestyle='--', color='orange', marker='o')
plt.legend()
plt.title("Prédiction avec une régression linéaire")
plt.xlabel("Date")
plt.ylabel("Ventes")
plt.grid()
plt.show()
