import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",
    temperature=0.1,
    api_key="AIzaSyDMOC1kuWVNsYlrT5VcMSiPIzqyA-JYsV8"
)
question=st.text_input('enter question.')
responce=llm.predict(question)
st.write(responce)
