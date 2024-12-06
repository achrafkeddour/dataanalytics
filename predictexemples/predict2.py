import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt

# Charger les données depuis un fichier CSV (ex. "open_data.csv")
# Assurez-vous que le fichier contient des colonnes "Date" et "Sales"
df = pd.read_csv("data2.csv")

# Prétraitement des données
df['Date'] = pd.to_datetime(df['Date'])  # Convertir les dates en format datetime
df.set_index('Date', inplace=True)  # Définir la colonne "Date" comme index
df = df.sort_index()  # Assurez-vous que les données sont triées par date

# Vérifiez les données
print(df.head())

# Ajustement du modèle ARIMA
model = ARIMA(df['Sales'], order=(1, 1, 1))  # Modèle simple ARIMA
model_fit = model.fit()

# Prédictions pour les 5 prochains jours
forecast = model_fit.forecast(steps=7)
future_dates = pd.date_range(start=df.index[-1] + pd.Timedelta(days=1), periods=7)
forecast_df = pd.DataFrame({'Date': future_dates, 'Forecast': forecast})
forecast_df.set_index('Date', inplace=True)

# Visualisation des données et des prévisions
plt.figure(figsize=(10, 5))
plt.plot(df['Sales'], label='Ventes historiques', marker='o')
plt.plot(forecast_df['Forecast'], label='Prévisions', linestyle='--', color='orange', marker='o')
plt.legend()
plt.title("Prédiction des ventes d'un produit à partir de données open data")
plt.xlabel("Date")
plt.ylabel("Ventes")
plt.grid()
plt.show()
