import streamlit as st
import pandas as pd
import altair as alt
from urllib.error import URLError

st.set_page_config(page_title="Griharaj: Insights", page_icon="📊")

st.markdown("# Properties Insights")
st.sidebar.header("Properties Insights")

df = pd.read_csv('Datasets/properties.csv')