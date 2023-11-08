import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

url = 'https://github.com/yahya-fa/dicodingproject/blob/main/hour.csv?raw=true'

df = pd.read_csv(url, index_col=0)

df = df.rename(columns= {'weathersit': 'weather',
                                   'yr': 'year',
                                   'mnth': 'month',
                                   'hr': 'hour',
                                   'hum': 'humidity',
                                   'cnt': 'count' })
df.head()

#df = df.drop(columns= ['instant','dteday', 'year'])

cols = ['season', 'month', 'hour', 'holiday', 'weekday', 'workingday', 'weather']
for col in cols:
    df[col] = df[col].astype('category')
#df.info()

st.header('Bike Sharing Dataset Analysis :sparkles:')

tab1, tab2, tab3 = st.tabs(["Analisis Berdasarkan perbedaan hari dan jam", "Analisis Berdasarkan perbedaan cuaca", "Analisis Berdasarkan perbedaan musim"])
with tab1:
    st.subheader('Jumlah Perentalan Sepeda Berdasarkan Perbedaan Hari ')
 
    fig, ax = plt.subplots(figsize=(20,10))
    sns.barplot(data=df, x='weekday', y='count', ax=ax)

    ax.set_ylabel(None)
    ax.set_xlabel("Weekdays (1-5) and Weekends (0,6)", fontsize=25)
    ax.tick_params(axis='y', labelsize=20)
    ax.tick_params(axis='x', labelsize=20)

    st.pyplot(fig)

    st.subheader('Peak Hours Total Perentalan Sepeda Berdasarkan Hari')
 
    fig, ax = plt.subplots(figsize=(20,10))
    sns.pointplot(data=df, x='hour', y='count', hue='weekday', ax=ax)

    ax.set_ylabel(None)
    ax.set_xlabel("Jam Penggunaan Rental", fontsize=25)
    ax.tick_params(axis='y', labelsize=20)
    ax.tick_params(axis='x', labelsize=20)

    st.pyplot(fig)

    st.subheader('Peak Hours Perentalan Sepeda Berdasarkan Hari dan User Non Member')
 
    fig, ax = plt.subplots(figsize=(20,10))
    sns.pointplot(data=df, x='hour', y='casual', hue='weekday', ax=ax)

    ax.set_ylabel(None)
    ax.set_xlabel("Jam Penggunaan Rental", fontsize=25)
    ax.tick_params(axis='y', labelsize=20)
    ax.tick_params(axis='x', labelsize=20)

    st.pyplot(fig)

    st.subheader('Peak Hours Perentalan Sepeda Berdasarkan Hari dan User Member')
 
    fig, ax = plt.subplots(figsize=(20,10))
    sns.pointplot(data=df, x='hour', y='registered', hue='weekday', ax=ax)

    ax.set_ylabel(None)
    ax.set_xlabel("Jam Penggunaan Rental", fontsize=25)
    ax.tick_params(axis='y', labelsize=20)
    ax.tick_params(axis='x', labelsize=20)

    st.pyplot(fig)

    with st.expander("Kesimpulan"):
        st.write(
            """jam teramai pada weekdays berdasarkan grafik semua pengguna dimulai dari pagi hari pada jam 6 dengan puncaknya pada jam 8 pagi dengan pengguna diangka 480an,
                 hal ini terjadi karena semua orang melakukan aktifitas yang sama yakni berangkat bekerja/sekolah. kemudian pada sore hari angka pengguna kembali naik di pukul 16.00 atau jam 4 sore dan puncaknya di jam 5 dan 6 sore,
                 hal ini terjadi dikarenakan pada sore dan malam hari orang-orang menggunakan rental untuk pulang bekerja dan mencari makan malam
            """
            )

with tab2:
    st.subheader('Jumlah Total Perentalan Sepeda Berdasarkan Cuaca')
 
    fig, ax = plt.subplots(figsize=(20,10))
    sns.pointplot(data=df, x='hour', y='count', hue='weather', ax=ax)

    ax.set_ylabel(None)
    ax.set_xlabel("Jam Penggunaan Rental", fontsize=25)
    ax.tick_params(axis='y', labelsize=20)
    ax.tick_params(axis='x', labelsize=20)

    st.pyplot(fig)

    st.subheader('Jumlah Perentalan Sepeda Berdasarkan Cuaca dan User Non Member')
 
    fig, ax = plt.subplots(figsize=(20,10))
    sns.pointplot(data=df, x='hour', y='casual', hue='weather', ax=ax)

    ax.set_ylabel(None)
    ax.set_xlabel("Jam Penggunaan Rental", fontsize=25)
    ax.tick_params(axis='y', labelsize=20)
    ax.tick_params(axis='x', labelsize=20)

    st.pyplot(fig)

    st.subheader('Jumlah Perentalan Sepeda Berdasarkan Cuaca dan User Member')
 
    fig, ax = plt.subplots(figsize=(20,10))
    sns.pointplot(data=df, x='hour', y='registered', hue='weather', ax=ax)

    ax.set_ylabel(None)
    ax.set_xlabel("Jam Penggunaan Rental", fontsize=25)
    ax.tick_params(axis='y', labelsize=20)
    ax.tick_params(axis='x', labelsize=20)

    st.pyplot(fig)

    with st.expander("Kesimpulan"):
        st.write(
            """pengaruh cuaca berbanding lurus terhadap jumlah perentalan, 
            berdasarkan grafik ketika cuaca bagus/cerah maka banyak orang akan melakukan perentalan sepeda 
            sedangkan jika cuaca sedang tidak bagus seperti saat mendung atau hujan maka jumlah pengguna akan menurun
            """
            )

with tab3:
    st.subheader('Jumlah Total Perentalan Sepeda Berdasarkan Musim')
 
    fig, ax = plt.subplots(figsize=(20,10))
    sns.pointplot(data=df, x='hour', y='count', hue='season', ax=ax)

    ax.set_ylabel(None)
    ax.set_xlabel("Jam Penggunaan Rental", fontsize=25)
    ax.tick_params(axis='y', labelsize=20)
    ax.tick_params(axis='x', labelsize=20)

    st.pyplot(fig)

    st.subheader('Jumlah Perentalan Sepeda Berdasarkan Musim dan User Non Member')
 
    fig, ax = plt.subplots(figsize=(20,10))
    sns.pointplot(data=df, x='hour', y='casual', hue='season', ax=ax)

    ax.set_ylabel(None)
    ax.set_xlabel("Jam Penggunaan Rental", fontsize=25)
    ax.tick_params(axis='y', labelsize=20)
    ax.tick_params(axis='x', labelsize=20)

    st.pyplot(fig)

    st.subheader('Jumlah Perentalan Sepeda Berdasarkan Musim dan User Member')
 
    fig, ax = plt.subplots(figsize=(20,10))
    sns.pointplot(data=df, x='hour', y='registered', hue='season', ax=ax)

    ax.set_ylabel(None)
    ax.set_xlabel("Jam Penggunaan Rental", fontsize=25)
    ax.tick_params(axis='y', labelsize=20)
    ax.tick_params(axis='x', labelsize=20)

    st.pyplot(fig)

    with st.expander("Kesimpulan"):
        st.write(
            """pengaruh cuaca terhadap jumlah perentalan berdasarkan grafik terjadi anomali 
            dimana pada musim semi jumlah pengguna memiliki nilai terendah diantara ketiga musim lainnya
            seperti musim panas, musim gugur, dan musim dingin. 
            perbedaan jumlah pengguna pada musim semi dengan musim dingin yang ranking jumlah penggunanya 1 tingkat diatasnya juga cukup signifikan, 
            yakni dapat mencapai lebih dari 370 ribu pengguna.
            """
            )       
