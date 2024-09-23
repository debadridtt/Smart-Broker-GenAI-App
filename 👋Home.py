import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px

df = pd.read_csv('properties.csv')

import streamlit as st

st.set_page_config(
    page_title="Griharaj",
    page_icon="👋",
)

st.write("# Griharaj: Welcome to GenAI powered Real Estate Investment Recommendation App! 👋")

st.image('images/img_1.jpg', width=300)