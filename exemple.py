import streamlit as st
import pandas as pd


st.title("nutrition_app")

csv_file = pd.read_csv("nutrition_databse.csv")
  
st.line_chart(df)
