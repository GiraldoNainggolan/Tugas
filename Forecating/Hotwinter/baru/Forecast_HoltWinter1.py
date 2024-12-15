import pandas as pd
import numpy as np
import streamlit as st

# Load dataset
def load_data(uploaded_file):
    df = pd.read_csv(uploaded_file)
    # Hanya gunakan kolom yang relevan
    return df[["year", "quartal", "aktual", "period"]]

# CRUD operations
def add_data(data, new_row):
    data = data.append(new_row, ignore_index=True)
    return data

def edit_data(data, index, updated_row):
    data.iloc[index] = updated_row
    return data

def delete_data(data, index):
    data = data.drop(index).reset_index(drop=True)
    return data

# Holt-Winters calculation (modified to match Excel logic)
def holt_winters(ts, alpha, beta, gamma, periods, forecast_steps):
    # Initialize parameters
    n = len(ts)
    level = [ts[0]]
    trend = [(ts[1] - ts[0])]
    season = [1] * periods  # Seasonal components
    forecast = []

    # Iterate through the time series
    for t in range(n):
        if t >= periods:
            season.append(gamma * (ts[t] - (level[-1] + trend[-1])) + (1 - gamma) * season[t % periods])
        else:
            season.append(1)

        if t > 0:
            level.append(alpha * (ts[t] - season[t % periods]) + (1 - alpha) * (level[-1] + trend[-1]))
            trend.append(beta * (level[-1] - level[-2]) + (1 - beta) * trend[-1])

    # Generate forecasts
    for t in range(forecast_steps):
        forecast.append(level[-1] + (t + 1) * trend[-1] + season[(n + t) % periods])

    return forecast

# Streamlit interface
st.title("Holt-Winters Forecasting")

# Upload file
uploaded_file = st.file_uploader("Upload your CSV file", type="csv")
if uploaded_file is not None:
    data = load_data(uploaded_file)
    st.write("### Data yang Diupload")
    st.dataframe(data)

    # CRUD Section
    st.write("### Edit Data")
    action = st.selectbox("Pilih Aksi", ["Tambah", "Edit", "Hapus"])

    if action == "Tambah":
        new_row = {
            "year": st.number_input("Year", step=1),
            "quartal": st.text_input("Quartal"),
            "aktual": st.number_input("Aktual", step=1.0),
            "period": st.number_input("Period", step=1)
        }
        if st.button("Tambah Data"):
            data = add_data(data, new_row)

    elif action == "Edit":
        index = st.number_input("Index", step=1, min_value=0, max_value=len(data) - 1)
        updated_row = {
            "year": st.number_input("Year", value=int(data.iloc[index]["year"]), step=1),
            "quartal": st.text_input("Quartal", value=data.iloc[index]["quartal"]),
            "aktual": st.number_input("Aktual", value=float(data.iloc[index]["aktual"]), step=1.0),
            "period": st.number_input("Period", value=int(data.iloc[index]["period"]), step=1)
        }
        if st.button("Update Data"):
            data = edit_data(data, index, updated_row)

    elif action == "Hapus":
        index = st.number_input("Index", step=1, min_value=0, max_value=len(data) - 1)
        if st.button("Hapus Data"):
            data = delete_data(data, index)

    st.write("### Data yang Diperbarui")
    st.dataframe(data)

    # Forecasting Section
    st.write("### Forecasting")
    ts = data["aktual"].astype(float).tolist()
    periods = 4  # Sesuai dengan data kuartal
    forecast_steps = 12  # Menampilkan 12 prediksi
    alpha, beta, gamma = 0.01, 0.01, 0.37

    if st.button("Run Forecast"):
        forecast = holt_winters(ts, alpha, beta, gamma, periods, forecast_steps)
        st.write("### Hasil Perhitungan Forecast")
        st.write("Prediksi:", forecast)
