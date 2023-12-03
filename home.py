import streamlit as st


st.set_page_config(
    page_title="Portfolio | Umi",
    page_icon="👨‍🎓",
    layout="wide"
)

st.title("SELAMAT DATANG DI PORTOFOLIO SAYA 👨‍🎓")

st.sidebar.success("SILAHKAN PILIH MENU DI ATAS")

import streamlit as st

col1, col2 = st.columns(2)

with col1:
   st.header("Tentang Saya")
   st.image("me.jpg", width= 390)

with col2:
   st.header("My Biodata")
   st.subheader("NAMA : UMI MASHLAHA FITRIYAH")
   st.caption("NIM : 0402201096")
   st.write(
            """
            - Tempat Tanggal Lahir : Brebes 18 Mei 2003 
            - Alamat               : Sengon Tanjung Brebes
            - Hobi                 : Membaca
            - Cita-cita            : Jadi Orang Manfaat

            """
        )
st.header("*Call Me If You Want*")
