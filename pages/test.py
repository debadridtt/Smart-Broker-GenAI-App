from langchain.agents import AgentType
# from langchain.agents import create_pandas_dataframe_agent
from langchain_experimental.agents import create_pandas_dataframe_agent
from langchain_google_genai import GoogleGenerativeAI
from langchain_google_genai.chat_models import ChatGoogleGenerativeAI
from langchain.callbacks import StreamlitCallbackHandler
from langchain.chat_models import ChatOpenAI
import streamlit as st
import pandas as pd
import os
from dotenv import load_dotenv
import os
import google.generativeai as genai
import pandas as pd
from contextlib import redirect_stdout
from io import StringIO
import streamlit as st
import numpy as np
from IPython.display import Markdown

file_formats = {
    "csv": pd.read_csv,
    "xls": pd.read_excel,
    "xlsx": pd.read_excel,
    "xlsm": pd.read_excel,
    "xlsb": pd.read_excel,
}


def clear_submit():
    """
    Clear the Submit Button State
    Returns:

    """
    st.session_state["submit"] = False


# @st.cache_data(ttl="2h")
# def load_data(uploaded_file):
#     try:
#         ext = os.path.splitext(uploaded_file.name)[1][1:].lower()
#     except:
#         ext = uploaded_file.split(".")[-1]
#     if ext in file_formats:
#         return file_formats[ext](uploaded_file)
#     else:
#         st.error(f"Unsupported file format: {ext}")
#         return None


st.set_page_config(page_title="LangChain: Chat with pandas DataFrame", page_icon="🦜")
st.title("🦜 LangChain: Chat with pandas DataFrame")

# uploaded_file = st.file_uploader(
#     "Upload a Data file",
#     type=list(file_formats.keys()),
#     help="Various File formats are Support",
#     on_change=clear_submit,
# )

# if not uploaded_file:
#     st.warning(
#         "This app uses LangChain's `PythonAstREPLTool` which is vulnerable to arbitrary code execution. Please use caution in deploying and sharing this app."
#     )

# if uploaded_file:
# df = load_data(uploaded_file)
df = pd.read_csv("Datasets/props cleaned.csv")

# openai_api_key = st.sidebar.text_input("OpenAI API Key", type="password")

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

if "messages" not in st.session_state or st.sidebar.button("Clear conversation history"):
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input(placeholder="What is this data about?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    # if not openai_api_key:
    #     st.info("Please add your OpenAI API key to continue.")
    #     st.stop()

    # llm = ChatOpenAI(
    #     temperature=0, model="gpt-3.5-turbo-0613", openai_api_key=openai_api_key, streaming=True
    # )

    api_key=os.getenv("GOOGLE_API_KEY")
    llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=api_key, temperature=0.2)

    pandas_df_agent = create_pandas_dataframe_agent(
        llm,
        df,
        verbose=True,
        agent_type="zero-shot-react-description", # AgentType.OPENAI_FUNCTIONS,
        handle_parsing_errors=True,
        allow_dangerous_code=True
    )

    with st.chat_message("assistant"):
        st_cb = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)
        response = pandas_df_agent.run(st.session_state.messages, callbacks=[st_cb])
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.write(response)