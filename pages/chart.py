import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner
import requests

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_url_hello = "https://lottie.host/2929245c-dd8a-4ecb-ba4b-fa5a2e5c4e39/ZB2FcZ2hNq.json"
lottie_hello = load_lottieurl(lottie_url_hello)


#การเรียกใช้งาาน lottie file
st_lottie(lottie_hello, key="hello")
st.balloons()

st.page_link("home.py", label="หน้าแรก", icon="🏠")
st.page_link("pages/statistic.py", label="การนำเสนอข้อมลด้วยสถิติ", icon="1️⃣")
st.page_link("pages/chart.py", label="การนำเสนอข้อมูลด้วยการจินตทัศ", icon="2️⃣", disabled=False)
st.page_link("http://www.google.com", label="Google", icon="🌎")