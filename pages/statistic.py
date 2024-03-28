import streamlit as st
import pandas as pd
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner
import requests

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_url_hello = "https://lottie.host/5f174efb-996c-4ab3-b3b4-dabd62c36e93/E345fQhWEP.json"
lottie_hello = load_lottieurl(lottie_url_hello)


#การเรียกใช้งาาน lottie file
st_lottie(lottie_hello, key="hello")
st.balloons()

st.page_link("home.py", label="หน้าแรก", icon="🏠")
st.page_link("pages/statistic.py", label="การนำเสนอข้อมลด้วยสถิติ", icon="1️⃣")
st.page_link("pages/chart.py", label="การนำเสนอข้อมูลด้วยการจินตทัศ", icon="2️⃣", disabled=False)
st.page_link("http://www.google.com", label="Google", icon="🌎")

dt = pd.read_csv('data/Dry_Bean_Dataset.csv')

st.subheader("ชุดข้อมูลถั่วแห้ง")
st.write(dt.head(10))

st.subheader("Solidity")
st.write('ค่ามากที่สุด')
cl21,cl22,cl23,cl24=st.columns(4)
cl21.write(dt['sepal.length'].max())
cl22.write(dt['sepal.width'].max())
cl23.write(dt['petal.length'].max())
cl24.write(dt['petal.width'].max())