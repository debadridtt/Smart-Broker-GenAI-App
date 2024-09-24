import streamlit as st
import pandas as pd
import altair as alt
from urllib.error import URLError
import plotly.express as px

st.set_page_config(page_title="Griharaj: Insights", page_icon="📊", layout='wide', initial_sidebar_state="auto")

st.markdown("### Available Properties Insights for Mumbai, India")
st.sidebar.header("Mumbai Properties Insights")

df = pd.read_csv('Datasets/properties.csv')
df = df[df['Possession Status'].isin(['Ready to Move', 'Under Construction'])]
df.reset_index(drop=True, inplace=True)
df_prop_type = df['Possession Status'].value_counts().to_frame().reset_index()

fig1 = px.pie(df_prop_type, values='count', names='Possession Status', title="Property Possession Type")


df_location_property_count = df.groupby(['Area Name'])['Units Available'].sum().to_frame().reset_index()
df_location_property_count = df_location_property_count.sort_values(by=['Units Available'], ascending=False)
df_location_property_count.reset_index(drop=True, inplace=True)
df_location_property_count = df_location_property_count[:10]


fig2 = px.bar(df_location_property_count, x='Area Name', y='Units Available', color='Area Name', title="Top 10 Areas with highest # of properties available")
fig2.update_xaxes(showticklabels=False)


cols = st.columns([1.25, 1])

cols[0].plotly_chart(fig1, theme=None, use_container_width = True)
cols[1].plotly_chart(fig2, theme=None)

possession_status = st.multiselect(
        "Choose Property Possession Status", list(df['Possession Status'].unique()), ["Ready to Move", "Under Construction"]
    )
if not possession_status:
    st.error("Please select at least one possession status")
else:
    data = df[df['Possession Status'].isin(['Ready to Move', 'Under Construction'])]
    data.reset_index(drop=True, inplace=True)