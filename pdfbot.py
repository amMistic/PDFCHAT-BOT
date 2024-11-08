import pdfplumber 
from langchain.text_splitter import RecursiveCharacterTextSplitter
from embeddings import embedding_function
from langchain_community.vectorstores.chroma import Chroma
from datetime import datetime
import os


# Extract the pdf content 
def extract_content(pdfs):
    content = ''
    for pdf in pdfs:
        with pdfplumber.open(pdf) as file:
            for page in file.pages:
                content += page.extract_text()
    return content

# Splitting down the content into chunks
def get_chunks(content):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size = 1000,
        chunk_overlap = 200,
        
    )
    chunks = splitter.split_text(content)
    return chunks

# convert each chunks into embedding vectors and stored it into vector store
def get_vector_store(pdfs):
    # extract
    content = extract_content(pdfs)
    
    # chunks
    chunks = get_chunks(content=content)
    
    # isolate unique
    uqid = datetime.now().strftime("%d%m%Y_%H%M%S")
    chroma = f'vecDatabase/{uqid}'
    os.makedirs(chroma, exist_ok=True)

    # store vector into vector store (chromaDB)
    vector_store = Chroma.from_texts(
        chunks,
        embedding=embedding_function(),
        persist_directory=chroma
    )
    
    return vector_store
    
    