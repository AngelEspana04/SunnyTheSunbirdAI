import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
from langchain.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
from HomeScreen import show_home_screen
from ChatScreen import show_chat_screen
from ChatTab import show_chat_tab 

# Initialize screen state if not already set
if "screen" not in st.session_state:
    st.session_state.screen = "home"  # Start at home screen

# Handle screen transitions based on the screen state
if st.session_state.screen == "chat":
    show_chat_screen()  # Show chat screen
else:
    show_home_screen()  # Show home screen
    
# Show the chat tab permanently at the bottom
show_chat_tab()

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Define path to the directory with your PDF files
PDF_DIRECTORY = "data"

# Function to read and extract text from all PDF files in the directory
def get_pdf_text_from_directory(pdf_directory):
    all_text = ""
    for filename in os.listdir(pdf_directory):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(pdf_directory, filename)
            pdf_reader = PdfReader(pdf_path)
            for page in pdf_reader.pages:
                all_text += page.extract_text()
    return all_text

def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
    return text_splitter.split_text(text)

def get_vector_store(text_chunks):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    vector_store.save_local("faiss_index")

# Load and process PDFs only once
if "faiss_index_built" not in st.session_state:
    pdf_text = get_pdf_text_from_directory(PDF_DIRECTORY)
    text_chunks = get_text_chunks(pdf_text)
    get_vector_store(text_chunks)
    st.session_state.faiss_index_built = True








   