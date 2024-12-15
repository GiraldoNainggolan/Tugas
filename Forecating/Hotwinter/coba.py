import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Fungsi CRUD menggunakan Pandas

def create_data(df, year, periode, aktual):
    """Menambahkan data baru ke DataFrame."""
    new_row = {'Year': year, 'Periode': periode, 'Aktual': aktual}
    df = df.append(new_row, ignore_index=True)
    return df

def read_data(df, year=None, periode=None):
    """Membaca data dari DataFrame berdasarkan filter."""
    if year is not None:
        df = df[df['Year'] == year]
    if periode is not None:
        df = df[df['Periode'] == periode]
    return df

def update_data(df, index, column, new_value):
    """Memperbarui data di DataFrame."""
    if index in df.index and column in df.columns:
        df.at[index, column] = new_value
    return df

def delete_data(df, index):
    """Menghapus data berdasarkan indeks."""
    if index in df.index:
        df = df.drop(index)
    return df

# Menambahkan fungsi tambahan untuk melihat semua data
def display_data(df, n=5):
    """Menampilkan beberapa baris data."""
    return df.head(n)

# Menampilkan dataset awal sebagai referensi
display_data(data)
