# Importer les bibliothèques nécessaires
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
import matplotlib.pyplot as plt

# Charger les données
df = pd.read_csv("data2.csv")
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# Normalisation des ventes
sales = df['Sales'].values.reshape(-1, 1)
scaler = MinMaxScaler()
scaled_sales = scaler.fit_transform(sales)

# Préparer les données pour le LSTM
look_back = 7
X, y = [], []
for i in range(len(scaled_sales) - look_back):
    X.append(scaled_sales[i:i+look_back])
    y.append(scaled_sales[i+look_back])
X, y = np.array(X), np.array(y)

# Construire et entraîner le modèle LSTM
model = Sequential([
    LSTM(50, input_shape=(look_back, 1)),
    Dense(1)
])
model.compile(optimizer='adam', loss='mse')
model.fit(X, y, epochs=10, batch_size=1)

# Prédire les 7 prochains jours
last_data = scaled_sales[-look_back:]
predictions = []
for _ in range(7):
    pred = model.predict(last_data.reshape(1, look_back, 1), verbose=0)
    predictions.append(pred[0, 0])
    last_data = np.append(last_data[1:], pred)

# Transformation inverse des prédictions
predictions = scaler.inverse_transform(np.array(predictions).reshape(-1, 1))

# Afficher les résultats
future_dates = pd.date_range(start=df.index[-1] + pd.Timedelta(days=1), periods=7)
plt.plot(df.index, df['Sales'], label='Ventes historiques', marker='o')
plt.plot(future_dates, predictions, label='Prévisions', linestyle='--', color='orange', marker='o')
plt.legend()
plt.title("Prédiction des ventes avec LSTM")
plt.xlabel("Date")
plt.ylabel("Ventes")
plt.grid()
plt.show()

# Afficher les prévisions
forecast = pd.DataFrame({'Date': future_dates, 'Prévisions': predictions.flatten()})
print(forecast)
