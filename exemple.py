import streamlit as st
import pandas as pd
import matplotlib


uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None :
  df = pd.read_csv(uploaded_file, sep="|")
  st.write(df)
  st.line_chart(df)
 
st.line_chart(df)
 
