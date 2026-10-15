import streamlit as st
import pandas as pd

# Mengatur konfigurasi halaman (opsional)
st.set_page_config(page_title="Dashboard Data Fiskal", layout="wide")

st.title("📊 Dashboard Data Fiskal")
st.write("Aplikasi ini membaca dataset `dataset_fiskal_97_hipoFull.csv` langsung dari GitHub.")

# Fungsi untuk memuat data (menggunakan cache agar tidak reload terus-menerus)
@st.cache_data
def load_data():
    # Menggunakan URL Raw dari GitHub
    url = "https://raw.githubusercontent.com/Alam-A99/DATAAKSI/main/dataset_fiskal_97_hipoFull.csv"
    
    # Membaca file CSV
    # Jika dataset dipisahkan dengan titik koma (;), tambahkan sep=';' di dalam read_csv
    df = pd.read_csv(url)
    return df

# Memuat data
with st.spinner('Sedang memuat data...'):
    df = load_data()

st.success('Data berhasil dimuat!')

# Menampilkan cuplikan data
st.subheader("Cuplikan Data (Dataset Head)")
st.dataframe(df.head(10))

# Menambahkan sidebar untuk informasi dataset
st.sidebar.header("Informasi Dataset")
st.sidebar.write(f"**Total Baris:** {df.shape[0]}")
st.sidebar.write(f"**Total Kolom:** {df.shape[1]}")

# Menampilkan statistik deskriptif
st.subheader("Statistik Deskriptif")
st.write(df.describe())

# Opsi interaktif untuk melihat kolom tertentu
st.subheader("Eksplorasi Kolom")
pilih_kolom = st.multiselect("Pilih kolom yang ingin ditampilkan:", df.columns.tolist(), default=df.columns.tolist()[:3])

if pilih_kolom:
    st.dataframe(df[pilih_kolom])