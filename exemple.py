import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px 

chunksize = 10 ** 6
with pd.read_csv(filename, chunksize=chunksize) as reader:
    for chunk in reader:
        process(chunk)
