import streamlit as st
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the question asked."),
        ("user", "Question: {question}")
    ]
)

st.title("LangChain Demo Chat App with gemma2:2b")

input_text = st.text_input("Write your prompt")

# LLM
llm = Ollama(model="gemma2:2b")

# Output Parser
output_parser = StrOutputParser()

# Chain
chain = prompt | llm | output_parser

if input_text:
    response = chain.invoke({"question": input_text})
    st.write(response)