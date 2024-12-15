import pandas as pd

def csv_to_xlsx(input_csv, output_xlsx):
    try:
        # Membaca file CSV dengan opsi tambahan untuk debugging
        df = pd.read_csv(input_csv, on_bad_lines="skip", encoding="utf-8")
        
        # Menyimpan data ke file XLSX
        df.to_excel(output_xlsx, index=False, engine="openpyxl")
        
        print(f"File berhasil dikonversi dari {input_csv} ke {output_xlsx}.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

# Ganti 'data_pengunjung.csv' dengan file Anda
csv_to_xlsx('data_pengunjung.csv', 'data_pengunjung.xlsx')
