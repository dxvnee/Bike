import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
sns.set(style='dark')

# Judul aplikasi
st.title("Dashboard Sepeda: Analisis Data Hari dan Jam")

# Upload file CSV untuk data hari
day_file = st.file_uploader("Upload file CSV untuk data hari", type=["csv"], key="day_file")

# Upload file CSV untuk data jam
hour_file = st.file_uploader("Upload file CSV untuk data jam", type=["csv"], key="hour_file")

# Jika ada file yang di-upload
if day_file is not None:
    # Membaca file CSV menjadi DataFrame
    day_df = pd.read_csv(day_file)

    # Mengubah kolom 'dteday' menjadi datetime
    day_df['dteday'] = pd.to_datetime(day_df['dteday'])

    # Menampilkan DataFrame
    st.write("Data Hari yang di-upload:")
    st.dataframe(day_df)

    # Menampilkan informasi DataFrame
    st.write("Informasi Data Hari:")
    st.write(day_df.describe(include='all'))

if hour_file is not None:
    # Membaca file CSV menjadi DataFrame
    hour_df = pd.read_csv(hour_file)

    # Mengubah kolom 'dteday' menjadi datetime
    hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])

    # Menampilkan DataFrame
    st.write("Data Jam yang di-upload:")
    st.dataframe(hour_df)

    # Menampilkan informasi DataFrame
    st.write("Informasi Data Jam:")
    st.write(hour_df.describe(include='all'))

# Analisis untuk data hari
if day_file is not None:
    st.subheader("Analisis Data Hari")
    analysis_type_day = st.selectbox("Pilih jenis analisis untuk data hari", ["Statistik Deskriptif", "Visualisasi"])

    if analysis_type_day == "Statistik Deskriptif":
        st.write("Statistik deskriptif dari kolom numerik:")
        st.write(day_df.describe())

    elif analysis_type_day == "Visualisasi":
        st.subheader("Visualisasi Data Hari")
        plt.figure(figsize=(10, 6))
        sns.barplot(data=day_df, x='weathersit', y='cnt', palette="Blues")
        plt.title("Rata-rata Jumlah Pengguna Sepeda Berdasarkan Cuaca")
        plt.xlabel("Situasi Cuaca")
        plt.ylabel("Jumlah Pengguna Sepeda")
        plt.xticks([0, 1, 2, 3], ['Clear/Partly Cloudy', 'Misty/Cloudy', 'Light Rain/Snow', 'Heavy Rain/Storm'])
        st.pyplot(plt)

# Analisis untuk data jam
if hour_file is not None:
    st.subheader("Analisis Data Jam")
    analysis_type_hour = st.selectbox("Pilih jenis analisis untuk data jam", ["Statistik Deskriptif", "Visualisasi"])

    if analysis_type_hour == "Statistik Deskriptif":
        st.write("Statistik deskriptif dari kolom numerik:")
        st.write(hour_df.describe())

    elif analysis_type_hour == "Visualisasi":
        st.subheader("Visualisasi Data Jam")
        plt.figure(figsize=(10, 6))
        sns.lineplot(data=hour_df, x='hr', y='cnt', marker='o')
        plt.title("Jumlah Pengguna Sepeda per Jam")
        plt.xlabel("Jam")
        plt.ylabel("Jumlah Pengguna Sepeda")
        plt.xticks(range(0, 24), [f"{i}:00" for i in range(24)])
        st.pyplot(plt)

# Pesan di bagian bawah
st.write("Silakan upload file CSV untuk memulai analisis!")
