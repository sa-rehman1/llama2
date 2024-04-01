# from langchain.llms import OpenAI
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
import os

#Prompt Template

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a help ful assistent"),
        ("user","Question:{question}")
    ]
)

#Streamlit frame work

st.title("Llama 2 chatbot")
input_text=st.text_input("Search for the topic you want")

llm=Ollama(model="llama2:13b")

output_parser=StrOutputParser()

chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))
