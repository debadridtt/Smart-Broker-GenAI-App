from dotenv import load_dotenv
import os
import google.generativeai as genai
import pandas as pd
from contextlib import redirect_stdout
from io import StringIO
import streamlit as st
import numpy as np
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

# def LLM_Response(question):
#     response = chat.send_message(question,stream=True)
#     return response

# input = st.text_input("Chat with Smart Broker to know about Real-estate market in Mumbai:", key="input")
# submit = st.button("Ask Question!")

# response = st.session_state.chat.send_message(input)
# response_markdown = Markdown(response.text).data

# with st.chat_message("assistant"):
# 	st.markdown(response_markdown)

df = pd.read_csv("Datasets/props cleaned.csv")
     
for message in st.session_state.chat.history:
    with st.chat_message(role_to_streamlit(message.role)):
        st.markdown(Markdown(message.parts[0].text).data)

if prompt := st.chat_input("I possess a well of knowledge. What would you like to know?"):
    st.chat_message("user").markdown(prompt)
    response = st.session_state.chat.send_message(prompt) 
    with st.chat_message("assistant"):
        st.markdown(response.text)

# if submit and input:
#         response = LLM_Response(input)
#         st.session_state['chat_history'].append(("You", input))
#         st.subheader("Response:")
#         for chunk in response:
#              st.write(chunk.text)
#              st.session_state['chat_history'].append(('Smart Broker', chunk.text))
# st.subheader('Chat History:')

# for role, text in st.session_state['chat_history']:
#      st.write(f"{role}:{text}")

# uploaded_file = st.file_uploader("Upload CSV/Excel file", type=["csv", "xlsx"])

# def get_gemini_response(Question):
#     response = model.generate_content(Question)
#     return f"{response.text}"

# if uploaded_file is not None:
#     if not os.path.isfile("D:/Downloads/" + uploaded_file.name):
#         st.error(f"Error: File '{uploaded_file.name}' does not exist.")
#         st.stop()



    # st.subheader("Top 5 Rows of the DataFrame:")
    # st.write(df.head(5))

# variable = st.text_input("Enter requirements to view recommended properties in Mumbai:")
# ask_question = st.button("Generate property recommendations!")

# if uploaded_file is not None:
#     question = f"use the dataframe with name df and columns ['Area Name', 'Description/Amenities', 'Price'] to generate pandas code " + variable \
#         + 'For a string column of a dataframe, to apply a filter use df[column].str.lower().str.contains() and for integer column use df[column] >=.\
#             In the filtered dataframe keep only columns [ID, Area Name, Developer, Description/Amenities, Price]. Print the dataframe'
        # + 'and return only\
        # developer, value, location, covered area, possession status, ID and units available columns'


# if ask_question:
#     question = f"use the dataframe with name df and columns ['Area Name', 'Developer', 'Description/Amenities', 'Price'] to generate pandas code " + variable \
#         + 'For a string column of a dataframe, to apply a filter use df[column].str.lower().str.contains() and for integer column use df[column] >=.\
#             In the filtered dataframe keep only columns [ID, Area Name, Developer, Description/Amenities, Price]. Print the dataframe'
#     response = LLM_Response(question)
#     # st.write(response)
#     st.subheader("The response is")
#     try:
#         start_index1 = response.find('#')
#         start_index2 = response.rfind(')')
#         exec_code = response[start_index1:start_index2 + 1]
#         with StringIO() as output_buffer:
#             with redirect_stdout(output_buffer):
#                 exec(exec_code)
#             captured_output = output_buffer.getvalue()
#     except:
#          captured_output = "No records found!"
#     st.code(captured_output, language='python')
