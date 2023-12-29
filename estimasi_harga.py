import streamlit as st
from streamlit_option_menu import option_menu
import pickle
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(
        page_title="Estimasi Harga Baru Berdasarkan Harga dari Kompetitor",
        page_icon="star",
        # layout="wide"
    )

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# st.title(f"Estimasi Harga berdasasrkan Harga dari Kompetitor")
st.markdown("<h2 class='title'>Estimasi Harga Produk Berdasarkan Harga dari Kompetitor ✨</h2>", unsafe_allow_html=True)

# 5. Add on_change callback
def on_change(key):
    selection = st.session_state[key]
    # st.write(f"Selection changed to {selection}")
    
selected = option_menu(None, ["Tentang","Visualisasi", "Model", "Estimasi"],
                        icons=['house','activity', 'info', "star"],
                        on_change=on_change, key='menu_5', orientation="horizontal",
                        styles={
        "container": {"padding": "0px!important", "border-color":"#f8fafc"},
        "icon": {"color": "#", "font-size": "25px"}, 
        "nav-link": {"color": "#f8fafc","font-size": "20px", "text-align": "center",   "margin":"0px", "--hover-color": "#","font-weight":"bold"},
        "nav-link-selected": {"background-color": "#e2e8f0", "color": "#1e293b"},
    })


if selected == "Tentang":
    st.markdown("<h3>👉 Model</h3>", unsafe_allow_html=True)
    st.markdown("<p style='font-size:18px;'>Aplikasi ini menggunakan model <b style='color:#fcd34d;'>Regresi Linier Berganda</b> yang memiliki akurasi sebesar <b style='color:#4ade80;'>89.97%</b> </p>", unsafe_allow_html=True)
    st.markdown("<h3>👉 Tujuan dan Manfaat</h3>", unsafe_allow_html=True)
    st.markdown("<p>Penggunaan model regresi linier berganda untuk mengestimasi harga terbaru dari produk pada perusahaan retail bertujuan agar perusahaan untuk mengerti bagaimana harga produk dari pesaing dapat mempengaruhi harga produk mereka. Sehingga perusahaan dapat mengestimasi harga untuk membuat keputusan harga yang lebih strategis untuk meningkatkan profit, serta merespon harga dari kompetitor.</p>", unsafe_allow_html=True)

if selected == "Visualisasi":
    st.markdown("<h3>👉 Deskripsi Dataset</h3>", unsafe_allow_html=True)
    st.markdown("<p>Data yang digunakan merupakan dataset private yang diperoleh dari perusahaan retail yang ada di Kota Semarang. Data Memiliki 6199 baris dan 4 atribut. Variabel bebas disini adalah atribut <b>Current Price</b> dan <b>Competitor Price</b> sedangkan variabel terikatnya atau labelnya adalah atribut <b>New Price</b>.</p>", unsafe_allow_html=True)
    df = pd.read_csv('product_price.csv') # Import dataset
    st.write(df)
    st.markdown("<h3>👉 Heatmap</h3>", unsafe_allow_html=True)
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.heatmap(df.isnull(), ax=ax)
    st.pyplot(fig)
    st.write("Hasil menunjukkan bahwa pada data tidak terdapat missing value, sehingga tidak perlu melakukan normalisasi")
    
    st.markdown("<h3>👉 Korelasi Antar Atribut</h3>", unsafe_allow_html=True)
    plt.figure(figsize=(10, 8))
    numeric_df = df.select_dtypes(include=['number'])
    heatmap = sns.heatmap(numeric_df.corr(), annot=True)
    st.pyplot(heatmap.figure)
    st.write("Dapat dilihat bahwa antar atribut atau variabel memiliki korelasi yang kuat, sehingga atribut memiliki hubungan satu sama lain.")
    
    st.markdown("<h3>👉 Plot Hubungan Antara Current Price dan Competitor Price Terhadap New Price</h3>", unsafe_allow_html=True)
    plt.figure(figsize=(10, 8))
    sns.pairplot(data=df, x_vars=['Current Price', 'Competitor Price'], y_vars=['New Price'], height=4, aspect=0.75)
    st.pyplot(plt)
    st.write("Dapat dilihat bahwa terdapat kecenderungan atau hubungan positif antara variabel current price dan competitor price. Berarti ketika nilai dari current price dan competitor meningkat, makan nilai dari new price cenderung juga meningkat.")
    
if selected == "Model":
    st.markdown("<h3 style='text-align:center'>Model Persamaan Regresi Linier Berganda</h3>", unsafe_allow_html=True)
    st.markdown("<p class='eq'>Y = 12885.33806335504 + 0.568937X1 + 0.364164X2</p>", unsafe_allow_html=True)
    st.markdown("<h3>📝 Keterangan: </h3>", unsafe_allow_html=True)
    st.markdown("<ul><li>Y = Harga baru</li><li>X1 = Harga saat ini</li><li>X2 = Harga kompetitor</li></ul>", unsafe_allow_html=True)
    
    st.markdown("<h3>🪄 Interpretasi Hasil Model </h3>", unsafe_allow_html=True)
    st.markdown("<h5 style='color:#fcd34d;'>Current Price </h5>", unsafe_allow_html=True)
    st.markdown("<p>Memiliki nilai positif sebesar 0.568937. Hal ini menunjukkan jika X1 mengalami kenaikan 1, maka Y akan naik sebesar 0.568937 dengan asumsi variabel independen lainnya dianggap konstan. Tanda positif artinya menunjukkan pengaruh yang searah antara variabel independen dan variabel dependen.</p>", unsafe_allow_html=True)
    st.markdown("<h5 style='color:#fcd34d;'>Competitor Price </h5>", unsafe_allow_html=True)
    st.markdown("<p>Memiliki nilai positif sebesar 0.364164. Hal ini menunjukkan jika X2 mengalami kenaikan 1, maka Y akan naik sebesar 0.364164 dengan asumsi variabel independen lainnya dianggap konstan. Tanda positif artinya menunjukkan pengaruh yang searah antara variabel independen dan variabel dependen.</p>", unsafe_allow_html=True)
    st.markdown("<h5 style='color:#fcd34d;'>Nilai Konstanta (a)</h5>", unsafe_allow_html=True)
    st.markdown("<p>Nilai konstanta (a) memiliki nilai positif sebesar 12885.33806335504. Tanda positif artinya menunjukkan pengaruh yang searah antara variabel independen dan variabel dependen. Hal ini menunjukkan bahwa jika semua variabel independen yang meliputi X1, dan X2, bernilai 0, maka Y secara rata-rata adalah 12885.33806335504.</p>", unsafe_allow_html=True)
    
    st.markdown("<p class ='conc'>Karena semua koefisien dalam model regresi bernilai positif, hal tersebut menunjukkan bahwa kenaikan nilai setiap harga saat ini (current price) dan harga kompetitor (competitor price) akan menyebabkan peningkatan nilai harga baru (new price).</p>", unsafe_allow_html=True)
    
    st.markdown("<h3>🎉 Evaluasi dan Kesimpulan </h3>", unsafe_allow_html=True)
    st.markdown("<p>Mean Squared Error (MSE) sebesar 4078034352.348392 menunjukkan tingkat kesalahan rata-rata kuadrat dari model. Semakin rendah MSE, semakin baik performa model.</p>", unsafe_allow_html=True)
    st.markdown("<p>R² Score sebesar 0.8996634586236606 mengindikasikan bahwa sekitar 89.97% variabel bebas dapat menjelaskan keragaman model. Sedangkan 10,03% lainnya dipengaruhi oleh faktor-faktor lain di luar variabel terikat.</p>", unsafe_allow_html=True)
    
    
    st.markdown("<p>Kesimpulan dari penggunaan model regresi linier berganda untuk mengestimasi harga baru produk berdasarkan harga dari kompetitor yaitu dengan melihat tingginya akurasi model (R² Score yang tinggi) maka perusahaan dapat menggunakan hasil model ini sebagai dasar untuk mengembangkan strategi harga yang lebih baik, yang memungkinkan mereka untuk membuat keputusan harga yang lebih strategis untuk meningkatkan profit, serta merespon harga dari kompetitor.</p>", unsafe_allow_html=True)
    

if selected == "Estimasi":
    model = pickle.load(open('estimasi_harga.sav', 'rb'))

# Form Inputan
    CurrentPrice = st.number_input("Input Harga Saat Ini")
    CompetitorPrice = st.number_input("Input Harga Kompetitor")
    predict = ''
    if st.button('Estimasi Harga Baru'):
        predict_list = model.predict(
        [[CurrentPrice, CompetitorPrice]]
        )
        predict = predict_list[0]
        st.markdown("<h5>Hasil Estimasi Harga Baru 🎈 </h5>", unsafe_allow_html=True)
        st.markdown(f"<p class='predict'>{predict}</p>", unsafe_allow_html=True)


st.markdown("<p class='cr'>© 2023 Taliya Meyswara (A11.2022.14163) - A11.43UG1</p>", unsafe_allow_html=True)