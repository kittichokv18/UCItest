import streamlit as st
import pandas as pd

st.title("website Developing using python")
#st.header("website Developing using python")

st.image('img/dance.gif')

dt=pd.read_csv('data/iris.csv')

st.subheader("ข้อมูลดอกไม้ Iris")
st.write(dt.head(10))

st.subheader("สถิติข้อมูลดอกไม้ Iris")
st.write("ผลรวม")
cl1,cl2,cl3,cl4=st.columns(4)
cl1.write("sepal.length")
cl1.write(dt['sepal.length'].sum())

cl2.write("sepal.width")
cl2.write(dt['sepal.width'].sum())

cl3.write("petal.length")
cl3.write(dt['petal.length'].sum())

cl4.write("petal.width")
cl4.write(dt['petal.width'].sum())

st.write("กราฟแท่ง")
a=dt['sepal.length'].sum()
b=dt['sepal.width'].sum()
c=dt['petal.length'].sum()
d=dt['petal.width'].sum()
dx=[a,b,c,d]
cx=pd.DataFrame(dx,index=["sepal.length", "sepal.width", "petal.length","petal.width"])
st.bar_chart(cx)

st.write("ค่าเฉลี่ย")
cl1,cl2,cl3,cl4=st.columns(4)
cl1.write(dt['sepal.length'].mean())
cl2.write(dt['sepal.width'].mean())
cl3.write(dt['petal.length'].mean())
cl4.write(dt['petal.width'].mean())

st.write("Area_Chart")
a=dt['sepal.length'].mean()
b=dt['sepal.width'].mean()
c=dt['petal.length'].mean()
d=dt['petal.width'].mean()
dxt=[a,b,c,d]
cxx=pd.DataFrame(dxt,index=["sepal.length", "sepal.width", "petal.length","petal.width"])
st.area_chart(cxx)

st.write("ค่ามากที่สุด")
cl1,cl2,cl3,cl4=st.columns(4)
cl1.write(dt['sepal.length'].max())
cl2.write(dt['sepal.width'].max())
cl3.write(dt['petal.length'].max())
cl4.write(dt['petal.width'].max())

import numpy as np
import matplotlib.pyplot as plt
labels = ['Sepal Length', 'Sepal Width', 'Petal Length', 'Petal Width']
sizes = [dt['sepal.length'].max(), dt['sepal.width'].max(), dt['petal.length'].max(), dt['petal.width'].max()]
explode = (0, 0.1,0,0) 
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
st.pyplot(fig1)

st.write("ค่าน้อยที่สุด")
cl1,cl2,cl3,cl4=st.columns(4)
cl1.write(dt['sepal.length'].min())
cl2.write(dt['sepal.width'].min())
cl3.write(dt['petal.length'].min())
cl4.write(dt['petal.width'].min())

st.write("Line_Chart")
cc= [dt['sepal.length'].min(), dt['sepal.width'].min(), dt['petal.length'].min(), dt['petal.width'].min()]
st.line_chart(cc)