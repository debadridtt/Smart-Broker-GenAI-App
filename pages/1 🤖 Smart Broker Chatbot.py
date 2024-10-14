from dotenv import load_dotenv
import os
import google.generativeai as genai
import streamlit as st
from IPython.display import Markdown

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

st.set_page_config(page_title="Smart Broker: Chat", page_icon="🤖", layout='wide', initial_sidebar_state="auto")
st.title("Welcome to Smart Broker Chat")

model = genai.GenerativeModel("gemini-pro")

def role_to_streamlit(role):
  if role == "model":
    return "assistant"
  else:
    return role

if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history = [])
     
for message in st.session_state.chat.history:
    with st.chat_message(role_to_streamlit(message.role)):
        st.markdown(Markdown(message.parts[0].text).data)

if prompt := st.chat_input("I possess knowledge related to real-estate market about Mumbai. What would you like to know?"):
    st.chat_message("user").markdown(prompt)
    response = st.session_state.chat.send_message(prompt) 
    with st.chat_message("assistant"):
        st.markdown(response.text)

