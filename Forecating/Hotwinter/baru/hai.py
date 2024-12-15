import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# Simulasi Dataframe awal
data = {
    'year': [2024]*12,
    'quartal': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    'aktual': [61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72],
    'period': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    'YLt - Yt': [61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72],  # Initial calculation
    'AT': [137.3629, 168.5788, 142.4593, 263.03, 339.7821, 360.4768, 354.9344, 316.556, 393.6195, 247.7476, 296.7755, 170.7504],
    'Tt': [137.3629, 168.5788, 142.4593, 263.03, 339.7821, 360.4768, 354.9344, 316.556, 393.6195, 247.7476, 296.7755, 170.7504],  # Same as AT in example
    'St': [137.3629, 168.5788, 142.4593, 263.03, 339.7821, 360.4768, 354.9344, 316.556, 393.6195, 247.7476, 296.7755, 170.7504],
    'Forecast': [137.3629, 168.5788, 142.4593, 263.03, 339.7821, 360.4768, 354.9344, 316.556, 393.6195, 247.7476, 296.7755, 170.7504]  # Initial prediction
}

df = pd.DataFrame(data)

# Pembersihan dan konversi ke format yang benar
df['Forecast'] = df['Forecast'].apply(lambda x: str(x).replace(',', '')).astype(float)

# Prediksi untuk 2024 menggunakan Holt-Winters atau metode lain, di sini kita menggunakan contoh sederhana
future_periods = 12
forecast_values = [df['Forecast'].iloc[-1]] * future_periods  # Menggunakan nilai terakhir sebagai forecast (gantilah ini dengan model yang lebih canggih)

# Data untuk prediksi 2024
future_data = {
    'year': [2024] * future_periods,
    'quartal': np.arange(1, future_periods + 1),
    'aktual': [np.nan] * future_periods,  # Prediksi tanpa data aktual
    'period': np.arange(13, 13 + future_periods),
    'YLt - Yt': [np.nan] * future_periods,  # Perhitungan lebih lanjut bisa ditambahkan
    'AT': forecast_values,
    'Tt': forecast_values,  # Asumsikan sama dengan AT untuk saat ini
    'St': forecast_values,
    'Forecast': forecast_values
}

future_df = pd.DataFrame(future_data)

# Gabungkan data historis dan prediksi untuk tampilkan
df_combined = pd.concat([df, future_df], ignore_index=True)

# Tampilkan data tabel
st.subheader("Prediksi 2024")
st.write(df_combined)

# Visualisasi data historis dan prediksi
st.subheader("Grafik Forecasting")
plt.figure(figsize=(10, 5))
plt.plot(df['period'], df['aktual'], label="Aktual", marker='o')
plt.plot(future_df['period'], future_df['Forecast'], label="Forecast 2024", linestyle="--")
plt.legend()
plt.xlabel("Period")
plt.ylabel("Values")
plt.xticks(rotation=45)
st.pyplot(plt)

# Tabel perhitungan langkah-demi-langkah
st.subheader("Perhitungan Langkah-demi-Langkah")
step_by_step_data = df_combined[['year', 'quartal', 'aktual', 'period', 'YLt - Yt', 'AT', 'Tt', 'St', 'Forecast']]
st.write(step_by_step_data)
