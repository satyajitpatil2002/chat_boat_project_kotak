


import os
import streamlit as st
from langchain.document_loaders import DirectoryLoader, PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.document_loaders import PyPDFLoader

os.environ["OPENAI_API_KEY"] = "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"

# Set persist directory
persist_directory = 'db'

Local_loader = PyPDFLoader('C:\\Users\\sanchit\\Downloads\\MBAGPT-main\\MBAGPT-main\\docs\\POC.pdf')

Local_docs = Local_loader.load()


embeddings = OpenAIEmbeddings()
text_splitter = CharacterTextSplitter(chunk_size=250, chunk_overlap=8)

# Split documents and generate embeddings
Local_docs_split = text_splitter.split_documents(Local_docs)


# Create Chroma instances and persist embeddings
LocalDB = Chroma.from_documents(Local_docs_split, embeddings, persist_directory=os.path.join(persist_directory, 'Local'))
LocalDB.persist()


