import streamlit as st
import pandas as pd
import altair as alt
from urllib.error import URLError
import plotly.express as px
import warnings
warnings.filterwarnings('ignore')

st.set_page_config(page_title="Smart Broker: Insights", page_icon="📊", layout='wide', initial_sidebar_state="auto")

st.markdown("### Insights of available properties in Mumbai, India")
st.sidebar.header("Mumbai Properties Insights")

df = pd.read_csv('Datasets/properties.csv')
df = df[df['Possession Status'].isin(['Ready to Move', 'Under Construction'])]
df.reset_index(drop=True, inplace=True)
df = df[df['Price'] <= 50000000]
df.reset_index(drop=True, inplace=True)

possession_status = st.multiselect(
        "Choose Property Possession Status", list(df['Possession Status'].unique()), []
    )
print(possession_status)
if possession_status:
    data = df[df['Possession Status'].isin(possession_status)]
    data.reset_index(drop=True, inplace=True)
else:
    data = df.copy()

price_range = st.slider("Select a price range", data['Price'].min(), data['Price'].max(), (data['Price'].min(), data['Price'].max()))

if price_range:
    data_p2 = data[data['Price'].between(price_range[0], price_range[1])]
    data_p2.reset_index(drop=True, inplace=True)
else:
    data_p2 = data.copy()

df_prop_type = data_p2['Possession Status'].value_counts().to_frame().reset_index()

fig1 = px.pie(df_prop_type, values='count', names='Possession Status', title="Property Possession Type")


df_location_property_count = data_p2.groupby(['Area Name'])['Units Available'].sum().to_frame().reset_index()
df_location_property_count = df_location_property_count.sort_values(by=['Units Available'], ascending=False)
df_location_property_count.reset_index(drop=True, inplace=True)
df_location_property_count = df_location_property_count[:10]


fig2 = px.bar(df_location_property_count, x='Area Name', y='Units Available', color='Area Name', title="Top 10 Areas with highest # of properties available")
fig2.update_xaxes(showticklabels=False)


cols = st.columns([1.25, 1])

cols[0].plotly_chart(fig1, theme=None, use_container_width = True)
cols[1].plotly_chart(fig2, theme=None)

data_p2 = data_p2[data_p2['Units Available'] >= 0]
data_p2.reset_index(drop=True, inplace=True)

data_p2 = data_p2[['ID', 'Possession Status', 'Price (English)', 'Area Name', 'Location', 'Floor No', 'Units Available', 'Covered Area', 'sqft Price ']]
st.write(data_p2)

def convert_to_csv(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv(index=False).encode('utf-8')

csv = convert_to_csv(df)

download1 = st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name='prop_list_df.csv',
    mime='text/csv'
)