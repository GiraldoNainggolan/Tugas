import pandas as pd
import streamlit as st
from statsmodels.tsa.holtwinters import ExponentialSmoothing

# Title
st.title("Aplikasi Forecasting Holt-Winters dengan CRUD dan Kuartal")

# Load data
uploaded_file = st.file_uploader("Unggah dataset CSV", type=["csv"])
if uploaded_file:
    data = pd.read_csv(uploaded_file)
    st.subheader("Dataset")
    st.dataframe(data)

    # CRUD
    st.sidebar.title("Manajemen Data")
    action = st.sidebar.selectbox("Pilih Aksi", ["Tambah Data", "Edit Data", "Hapus Data"])

    if action == "Tambah Data":
        st.sidebar.subheader("Tambah Data Baru")
        tahun = st.sidebar.number_input("Tahun", min_value=1900, max_value=2100, step=1)
        kuartal = st.sidebar.selectbox("Kuartal", list(range(1, 13)))
        nilai = st.sidebar.number_input("Nilai", min_value=0.0)
        if st.sidebar.button("Simpan"):
            tanggal = f"{tahun}-{kuartal:02d}-01"
            new_data = {"Tanggal": tanggal, "Nilai": nilai}
            data = pd.concat([data, pd.DataFrame([new_data])], ignore_index=True)
            st.success("Data berhasil ditambahkan!")

    elif action == "Edit Data":
        st.sidebar.subheader("Edit Data")
        index = st.sidebar.number_input("Index Data untuk Diedit", min_value=0, max_value=len(data) - 1, step=1)
        tahun = st.sidebar.number_input("Tahun Baru", min_value=1900, max_value=2100, step=1)
        kuartal = st.sidebar.selectbox("Kuartal Baru", list(range(1, 13)))
        nilai = st.sidebar.number_input("Nilai Baru", min_value=0.0, value=data.iloc[index]["Nilai"])
        if st.sidebar.button("Update"):
            tanggal = f"{tahun}-{kuartal:02d}-01"
            data.at[index, "Tanggal"] = tanggal
            data.at[index, "Nilai"] = nilai
            st.success("Data berhasil diperbarui!")

    elif action == "Hapus Data":
        st.sidebar.subheader("Hapus Data")
        index = st.sidebar.number_input("Index Data untuk Dihapus", min_value=0, max_value=len(data) - 1, step=1)
        if st.sidebar.button("Hapus"):
            data = data.drop(index).reset_index(drop=True)
            st.success("Data berhasil dihapus!")

    # Forecasting
    st.subheader("Forecasting Holt-Winters")
    period = st.number_input("Periode Musiman", min_value=1, step=1)
    ahead = st.number_input("Jumlah Prediksi ke Depan", min_value=1, step=1)
    mtype = st.selectbox("Metode", ["additive", "multiplicative"])

    if st.button("Prediksi"):
        try:
            data["Tanggal"] = pd.to_datetime(data["Tanggal"])
            data = data.sort_values("Tanggal")
            ts = data["Nilai"]

            # Model Holt-Winters
            model = ExponentialSmoothing(ts, seasonal=mtype, seasonal_periods=period)
            fit = model.fit()

            # Forecasting
            forecast = fit.forecast(steps=ahead)
            st.write("Hasil Prediksi:", forecast.tolist())

            # Tambahkan prediksi ke dataset
            pred_tanggal = pd.date_range(start=data["Tanggal"].max(), periods=ahead + 1, freq='M')[1:]
            pred_df = pd.DataFrame({"Tanggal": pred_tanggal, "Nilai": forecast.tolist()})
            data = pd.concat([data, pred_df], ignore_index=True)
            st.success("Prediksi berhasil ditambahkan ke dataset!")
        except Exception as e:
            st.error(f"Terjadi kesalahan: {e}")

    # Menampilkan data setelah perubahan
    st.subheader("Dataset Setelah Perubahan")
    st.dataframe(data)

    # Unduh dataset
    st.download_button(
        label="Unduh Dataset sebagai CSV",
        data=data.to_csv(index=False).encode('utf-8'),
        file_name="hasil_forecasting.csv",
        mime="text/csv",
    )