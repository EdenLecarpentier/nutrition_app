import streamlit as st
import pandas as pd


uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None :
  df = pd.read_csv(uploaded_file, sep="|")
  st.write(df)
  st.line_chart(df)
  
z = z_data.values
sh_0, sh_1 = z.shape
x, y = np.linspace(0, 1, sh_0), np.linspace(0, 1, sh_1)
fig = go.Figure(data=[go.Surface(z=z, x=x, y=y)])
fig.update_layout(title=‘IRR’, autosize=False,
width=800, height=800,
margin=dict(l=40, r=40, b=40, t=40))
st.plotly_chart(fig)
