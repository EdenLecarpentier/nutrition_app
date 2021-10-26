import streamlit as st
import pandas as pd
import plotly.express as px

st.title("nutrition_app")

def load_data():
  csv_file = pd.read_csv("nutrition_databse.csv")
  
def first_plot():
  st.line_chart(load_data)
  
