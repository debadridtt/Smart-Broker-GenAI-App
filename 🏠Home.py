import streamlit as st
import pandas as pd
import altair as alt
import plotly.express as px

st.set_page_config(
    page_title="Smart Broker",
    page_icon="🏠",
)

st.write("# Welcome to Smart Broker🏠")

col1, col2, col3 = st.columns(3)

with col1:
    st.write(' ')

with col2:
    st.image('images/img_1.jpg', width=200)

with col3:
    st.write(' ')

st.markdown(
    """
    **Smart Broker** is a GenAI powered chatbot and dashboard app framework built specifically to help customers
    take the right decisions for real-estate investments.

    **👇 Select the following options from below** to see explore the app!

    ### What is the functionality of Smart Broker Chatbot?

    - Check out [Smart Broker Chatbot](http://localhost:8501/Smart_Broker_Chatbot)
    - Chat with our GenAI agent to understand demographics, top locations around the city, Y-o-Y growth of real-estate prices, further development prospects, etc.
    - Finally use the chatbot messages to shortlist locations, requirements, budget, amenities for properties, etc.


    ### What is the functionality of Smart Broker Dashboard?

    - Check out [Smart Broker Dashboard](http://localhost:8501/Smart_Broker_Dashboard)
    - Dashbaord visualizes information related to different properties across Mumbai, India
    - Use information gathered from Chatbot to find the ideal property for investment or for staying

    ### Real-estate Market Cap in India: 
     
    Real estate sector in India is expected to reach USD 1 trillion in market size by 2030, up from USD 200 billion in 2021 and contribute 13% to the country’s GDP by 2025. Retail, hospitality, and commercial real estate are also growing significantly, providing the much-needed infrastructure for India's growing needs.
    India’s real estate sector is expected to expand to USD 5.8 trillion by 2047, contributing 15.5% to the GDP from an existing share of 7.3%.
    
    In FY23, India’s residential property market witnessed with the value of home sales reaching an all-time high of Rs. 3.47 lakh crore (USD 42 billion), marking a robust 48% YoY increase. The volume of sales also exhibited a strong growth trajectory, with a 36% rise to 379,095 units sold.
    Indian real estate developers operating in the country’s major urban centers are poised to achieve a significant feat in 2023, with the completion of approximately 558,000 homes.
    In 2023, demand for residential properties surged in the top 8 Indian cities, driven by mid-income, premium, and luxury segments despite challenges like high mortgage rates and property prices.
    [Reference](https://www.ibef.org/industry/real-estate-india) 
"""
)

