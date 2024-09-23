import streamlit as st
import pandas as pd
import altair as alt
from urllib.error import URLError

st.set_page_config(page_title="Griharaj: Insights", page_icon="📊")

st.markdown("# Properties Insights")
st.sidebar.header("Properties Insights")

df = pd.read_csv('Datasets/properties.csv')
df = df[df['Possession Status'].isin(['Ready to Move', 'Under Construction'])]
df.reset_index(drop=True, inplace=True)

possesstion_status = st.multiselect(
        "Choose Property Possession Status", list(df['Possession Status'].unique()), ["Ready to Move", "Under Construction"]
    )