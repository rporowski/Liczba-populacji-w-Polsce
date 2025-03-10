# -*- coding: utf-8 -*-
"""With ARIMA.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1lf9wYS_SVryKVEPtXxHbUSW5iTsEc_f7
"""

# Instalacja biblioteki pmdarima (jeśli nie jest zainstalowana)
!pip install pmdarima --quiet

# Import wymaganych bibliotek
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pmdarima import auto_arima
import warnings
warnings.filterwarnings("ignore")

# -----------------------------
# Tworzymy dane – przykładowy szereg czasowy (dane miesięczne, w tysiącach)
data = {
    "Data": [
        "2022-01-01", "2022-02-01", "2022-03-01", "2022-04-01", "2022-05-01", "2022-06-01",
        "2022-07-01", "2022-08-01", "2022-09-01", "2022-10-01", "2022-11-01", "2022-12-01",
        "2023-01-01", "2023-02-01", "2023-03-01", "2023-04-01", "2023-05-01", "2023-06-01",
        "2023-07-01", "2023-08-01", "2023-09-01", "2023-10-01", "2023-11-01", "2023-12-01",
        "2024-01-01", "2024-02-01", "2024-03-01", "2024-04-01", "2024-05-01"
    ],
    "Population": [
        37884, 37866, 37852, 37841, 37833, 37827,
        37823, 37815, 37807, 37795, 37785, 37766,
        37750, 37739, 37727, 37717, 37707, 37698,
        37692, 37686, 37679, 37667, 37654, 37637,
        37620, 37606, 37595, 37582, 37571
    ]
}

# Utworzenie DataFrame
df = pd.DataFrame(data)
df["Data"] = pd.to_datetime(df["Data"])
df.set_index("Data", inplace=True)
df.sort_index(inplace=True)

# Ustawienie częstotliwości szeregu czasowego na miesiąc (MS - początek miesiąca)
df = df.asfreq('MS')

# Interpolacja brakujących danych (jeśli występują)
df["Population"] = df["Population"].interpolate()

print("Dane historyczne (populacja Polski):")
print(df.head())

# -----------------------------
# Budowa modelu ARIMA z sezonowością (m=12)
model = auto_arima(
    df["Population"],
    start_p=1, start_q=1,
    max_p=3, max_q=3,
    seasonal=True,
    m=12,
    d=None,    # auto-determinuje wartość d
    D=1,       # sezonowe różnicowanie
    trace=False,
    error_action='ignore',
    suppress_warnings=True,
    stepwise=True
)

print("\nPodsumowanie modelu ARIMA:")
print(model.summary())

# -----------------------------
# Prognoza do 2035 roku
last_date = df.index[-1]  # Ostatni miesiąc danych (np. 2024-05-01)
forecast_horizon = (2035 - last_date.year) * 12 + (12 - last_date.month)
print(f"\nPrognozujemy na kolejne {forecast_horizon} miesięcy.")

forecast = model.predict(n_periods=forecast_horizon)
future_dates = pd.date_range(last_date + pd.offsets.MonthBegin(1), periods=forecast_horizon, freq='MS')
forecast_df = pd.DataFrame(forecast, index=future_dates, columns=["Forecast"])

# -----------------------------
# Wizualizacja wyników
plt.figure(figsize=(12, 6))
plt.plot(df.index, df["Population"], marker="o", label="Dane historyczne")
plt.plot(forecast_df.index, forecast_df["Forecast"], linestyle="--", color="red", label="Prognoza ARIMA")
plt.axvline(x=last_date, color="gray", linestyle="--", label="Koniec danych historycznych")
plt.title("Prognoza liczby ludności w Polsce do 2035 r. (model ARIMA)")
plt.xlabel("Rok")
plt.ylabel("Liczba ludności (w tysiącach)")
plt.legend()
plt.grid(True)
plt.show()

# -----------------------------
# Wnioski (po polsku)
print("\nWNIOSEK:")
print("Model ARIMA oparty na danych z lat 2022-2024 prognozuje, że liczba ludności Polski będzie kontynuować trend spadkowy do 2035 r. "
      "Wykres prognozy pokazuje, że populacja systematycznie maleje. "
      "Należy jednak pamiętać, że prognoza bazuje wyłącznie na historycznych danych szeregów czasowych i nie uwzględnia zmian demograficznych, migracyjnych ani polityk społeczno-ekonomicznych. Wynik należy traktować jako orientacyjny.")