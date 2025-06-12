from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
import os

load_dotenv() # take env variables from .env


## function to open AI model and get responses

def get_openai_response(question):
    if not question.strip():
        return "Please enter a prompt."
    llm = ChatOpenAI(openai_api_key = os.getenv("OPENAI_API_KEY"), model_name = "gpt-4.1-nano", temperature = 0.5, max_tokens=75)
    response = llm.invoke(question)
    return response.content

## initialise streamlit app

st.set_page_config(page_title = "Q&A ChatBot")
st.header("ChatBot")

input = st.text_input("Input:")

submit = st.button("Ask a question")

if submit or input.strip():
    response = get_openai_response(input)
    st.subheader("The response is")
    st.write(response)

