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

html_1 = """
<div style="background-color:#52BE80;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
<center><h5>สถิติข้อมูลดอกไม้</h5></center>
</div>
"""
st.markdown(html_1, unsafe_allow_html=True)
st.markdown("")


st.page_link("home.py", label="หน้าแรก", icon="🏠")
st.page_link("pages/statistic.py", label="การนำเสนอข้อมลด้วยสถิติ", icon="1️⃣")
st.page_link("pages/chart.py", label="การนำเสนอข้อมูลด้วยการจินตทัศ", icon="2️⃣", disabled=False)
st.page_link("http://www.google.com", label="Google", icon="🌎")

dt = pd.read_csv('data/Dry_Bean_Dataset.csv')

st.subheader("ชุดข้อมูลถั่วแห้ง")
st.write(dt.head(10))

st.subheader("max")
st.write('ค่ามากที่สุด')
max_values = dt.drop('Class', axis=1).max()

# สร้าง DataFrame สำหรับแสดงค่าสูงสุด
max_df = pd.DataFrame({"Column": max_values.index, "Max Value": max_values.values})

# แสดงตาราง
st.subheader("ตารางแสดงค่าสูงสุดของแต่ละคอลัมน์")
st.dataframe(max_df)

max_solidity_row = dt.loc[dt['Solidity'].idxmax()]
st.subheader("ข้อมูลมากที่สุดของ Solidity")
st.write("ค่า Solidity มากที่สุด:", max_solidity_row['Solidity'])
st.write("คลาส:", max_solidity_row['Class'])

max_AspectRation_row = dt.loc[dt['AspectRation'].idxmax()]
st.subheader("ข้อมูลมากที่สุดของ AspectRation")
st.write("ค่า AspectRation มากที่สุด:", max_AspectRation_row['AspectRation'])
st.write("คลาส:", max_AspectRation_row['Class'])