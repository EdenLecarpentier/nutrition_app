import streamlit as st

st.title("nutrition_app")

def load_data():
  csv_file = pd.read_csv("nutrition_databse.csv")
