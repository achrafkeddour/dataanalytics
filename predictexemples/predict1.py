import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt

# Création des données de ventes
dates = [
    "2023-01-01", "2023-01-02", "2023-01-03", "2023-01-04", "2023-01-05",
    "2023-01-06", "2023-01-07", "2023-01-08", "2023-01-09", "2023-01-10"
]
sales = [100, 110, 105, 108, 102, 115, 120, 118, 113, 125]

# Création d'un DataFrame pour organiser les données
df = pd.DataFrame({'Date': dates, 'Sales': sales})
print(df)

df['Date'] = pd.to_datetime(df['Date'])  # Convertir les dates en format Date
df.set_index('Date', inplace=True)  # Définir la colonne "Date" comme index

# Ajustement du modèle ARIMA
model = ARIMA(df['Sales'], order=(1, 1, 1))  # Modèle simple ARIMA
model_fit = model.fit()

# Prédictions pour les 5 prochains jours
forecast = model_fit.forecast(steps=5)
future_dates = pd.date_range(start=df.index[-1] + pd.Timedelta(days=1), periods=5)
forecast_df = pd.DataFrame({'Date': future_dates, 'Forecast': forecast})
forecast_df.set_index('Date', inplace=True)

# Visualisation des données et des prévisions
plt.figure(figsize=(10, 5))
plt.plot(df['Sales'], label='Ventes historiques', marker='o')
plt.plot(forecast_df['Forecast'], label='Prévisions', linestyle='--', color='orange', marker='o')
plt.legend()
plt.title("Prédiction des ventes d'un produit")
plt.xlabel("Date")
plt.ylabel("Ventes")
plt.grid()
plt.show()
