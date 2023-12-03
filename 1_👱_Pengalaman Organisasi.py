import streamlit as st
# SILAHKAN DI GANTI 2

st.set_page_config(
    page_title="Organizational Experience|Umi",
    page_icon="👨‍🎓",
    layout="wide"
)

st.title("Pengalaman Organisasi Pesantren")


st.container()
col1, = st.columns(1)
with col1:
    st.subheader("Pesantren Putri Al Bukhori")
   

st.container()
st.write("---")
col1, = st.columns(1)
with col1:
   
    st.image("pp.png.jpg", width= 190)

st.container()
st.write("---")
col1, = st.columns(1)
with col1:
    st.write("*Menjabat Sebagai K.a Keamanan Pesantren*")
   