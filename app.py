import os
import streamlit as st
import google.generativeai as genai
import time
from langchain_groq import ChatGroq
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Load the GROQ and Google Generative AI embeddings
groq_api_key = os.getenv("GROQ_API_KEY")
os.environ['GOOGLE_API_KEY'] = os.getenv("GOOGLE_API_KEY")

# Streamlit Title
st.title("Gemma Model Document Q&A")

# Initialize the Language Model
llm = ChatGroq(groq_api_key=groq_api_key, model_name="Gemma-7b-it")

# Define the Prompt Template
prompt = ChatPromptTemplate.from_template(
"""
Answer the question based on the provided context only.
Please provide the most accurate response based on the question.
<context>
{context}
<context>
Question: {input}
"""
)

# Function to Create Vector Embedding
def vector_embedding():
    if "vectors" not in st.session_state:
        
        st.session_state.embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
        st.session_state.loader = PyPDFDirectoryLoader("./us_census")
        st.session_state.docs = st.session_state.loader.load()
        st.session_state.text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        st.session_state.final_documents = st.session_state.text_splitter.split_documents(st.session_state.docs)
        st.session_state.vectors = FAISS.from_documents(st.session_state.final_documents, st.session_state.embeddings)
        

# User Input for Query
prompt1 = st.text_input("What You Want to ask From The Documents?")

# Button to Create Vector Store
if st.button("Creating Vector Store"):
    vector_embedding()
    st.write("vector store DB is ready")
import time

# Process User Query
if prompt1:
  
    document_chain = create_stuff_documents_chain(llm, prompt)
    retriever = st.session_state.vectors.as_retriever()  # Correct method
    retrieval_chain = create_retrieval_chain(retriever, document_chain)

    start = time.process_time()
    response = retrieval_chain.invoke({'input': prompt1})
    st.write(response.get('answer'))

    # Display Relevant Document Chunks
    with st.expander("Document Similarity Search"):
               
        for i, doc in enumerate(response["context"]):
            st.write(doc.page_content)
            st.write("-----------------------")




    