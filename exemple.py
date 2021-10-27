import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px 

st.set_option('deprecation.showPyplotGlobalUse', False)
st.title("Hello world!")

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None
  df = pd.read_csv(uploaded_file, sep="|")
  st.write(df)

fig, ax = plt.subplots()
 df.hist(
  bins=8,
  column="salt_100g",
  grid=False,
  figsize=(7, 7),
  color="Orange",
  zorder=2,
  rwidth=09,
  ax=ax,
)
write(fig)
