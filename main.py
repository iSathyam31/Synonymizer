import streamlit as st
from langchain_community.chat_models import ChatOllama
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import BaseOutputParser

class Commaseparatedoutput(BaseOutputParser):
    def parse(self, text: str):
        return text.strip().split(",")

# Set up Streamlit UI
st.set_page_config(page_title="Synonyms Generator", page_icon="🔄")

# Define the template for the chat prompt
template = "You are a helpful assistant. When the user provides any input, you should generate 5 words synonyms in a comma-separated list."
human_template = "{text}"

# Create the ChatPromptTemplate
chat_prompt = ChatPromptTemplate.from_messages([
    ("system", template),
    ("human", human_template)
])

# Create the ChatOpenAI model
model = Ollama(model="llama3")

# Create the chain
chain = chat_prompt | model | Commaseparatedoutput()

# Page header
st.header("🌟 Synonyms Generator ✏️")

# Description
st.write("Welcome to the Synonyms Generator! Enter any word or phrase to get 5 synonyms instantly. 🌟")

# Text input for user query
input_text = st.text_input("Enter a word or phrase:", "")

# Button to trigger the synonym generation
if st.button("Generate Synonyms 🚀"):
    # Perform the conversation with the chatbot
    if input_text:
        # Get the chatbot response
        response = chain.invoke({"text": input_text})

        # Display the synonyms
        st.success("Synonyms: 🌟 " + ", ".join(response))
    else:
        st.error("Please enter a word or phrase to get synonyms. ❗")

# Add a footer with some emojis
st.markdown("""
    <style>
        .footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            background-color: #f1f1f1;
            text-align: center;
            padding: 10px;
            color: black;
        }
    </style>
    <div class="footer">
        Made with by Sathyam A | Follow me on GitHub 🔗 | Contact me at Email:sathyama0302@gmail.com 📧
    </div>
""", unsafe_allow_html=True)

# Custom CSS for better UI
st.markdown("""
    <style>
        .stButton button {
            background-color: #4CAF50; /* Green */
            border: none;
            color: white;
            padding: 15px 32px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
            border-radius: 12px;
        }
        .stTextInput input {
            padding: 10px;
            font-size: 16px;
            border-radius: 12px;
            border: 2px solid #ccc;
        }
        .stHeader, .stMarkdown {
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)
