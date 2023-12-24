import streamlit as st
from streamlit_option_menu import option_menu
import pickle

st.set_page_config(
        page_title="Estimasi Harga Baru Berdasarkan Harga dari Kompetitor",
        page_icon="star"
    )

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# st.title(f"Estimasi Harga berdasasrkan Harga dari Kompetitor")
st.markdown("<h2 class='title'>Estimasi Harga Produk Berdasarkan Harga dari Kompetitor ✨</h2>", unsafe_allow_html=True)

# 5. Add on_change callback
def on_change(key):
    selection = st.session_state[key]
    # st.write(f"Selection changed to {selection}")
    
selected = option_menu(None, ["Tentang", "Persamaan", "Estimasi"],
                        icons=['house', 'info', "star"],
                        on_change=on_change, key='menu_5', orientation="horizontal",
                        styles={
        "container": {"padding": "0px!important", "border-color":"#f8fafc"},
        "icon": {"color": "#", "font-size": "25px"}, 
        "nav-link": {"color": "#f8fafc","font-size": "20px", "text-align": "center",   "margin":"0px", "--hover-color": "#","font-weight":"bold"},
        "nav-link-selected": {"background-color": "#e2e8f0", "color": "#1e293b"},
    })


if selected == "Tentang":
    st.markdown("<h3>👉 Model</h3>", unsafe_allow_html=True)
    st.markdown("<p style='font-size:18px;'>Aplikasi ini menggunakan model <b style='color:#fcd34d;'>Regresi Linier Berganda</b> yang memiliki akurasi sebesar <b style='color:#4ade80;'>89.97%</b></p>", unsafe_allow_html=True)
    st.markdown("<h3>👉 Tujuan dan Manfaat</h3>", unsafe_allow_html=True)
    st.markdown("<p>Penggunaan model regresi linier berganda untuk mengestimasi harga terbaru dari produk pada perusahaan retail bertujuan agar perusahaan untuk mengerti bagaimana harga produk dari pesaing dapat mempengaruhi harga produk mereka. Sehingga perusahaan dapat mengestimasi harga untuk membuat keputusan harga yang lebih strategis untuk meningkatkan profit, serta merespon harga dari kompetitor.</p>", unsafe_allow_html=True)
    
if selected == "Persamaan":
    # st.latex(r'''Y = 12885.33806335504 + 0.568937X1 + 0.364164X2''')
    st.markdown("<h3 style='text-align:center'>Model Persamaan Regresi Linier Berganda</h3>", unsafe_allow_html=True)
    st.markdown("<p class='eq'>Y = 12885.33806335504 + 0.568937X1 + 0.364164X2</p>", unsafe_allow_html=True)
    st.markdown("<h3>📝 Keterangan: </h3>", unsafe_allow_html=True)
    st.markdown("<ul><li>Y = Harga baru</li><li>X1 = Harga saat ini</li><li>X2 = Harga kompetitor</li></ul>", unsafe_allow_html=True)
    st.markdown("<p>Karena semua koefisien dalam model regresi bernilai positif, hal tersebut menunjukkan bahwa kenaikan nilai setiap harga saat ini (current price) dan harga kompetitor (competitor price) akan menyebabkan peningkatan nilai harga baru (new price).</p>", unsafe_allow_html=True)

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
        # st.write('', predict)


st.markdown("<p class='cr'>© 2023 Taliya Meyswara (A11.2022.14163) - A11.43UG1</p>", unsafe_allow_html=True)