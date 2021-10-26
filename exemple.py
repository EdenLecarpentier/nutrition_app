#pip
pip install plotly

#Streamlit
import streamlit as st
st.title("nutrition_app")

#Librairies
import pandas as pd
import plotly.express as px

#Dataset
df = pd.read_csv("C:/Users/zaome/Documents/Alisson/Nutrition/database_clean.csv", sep="|")
df.head()

#Correlation
corr = df.corr()
px.imshow(corr)
