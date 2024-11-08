# PDFBOT 🤖

Welcome to **PDFBOT**! This project allows users to upload PDFs and interact with their content through a chatbot interface. It uses large language models to respond to user queries based on the PDF's content, providing an engaging and interactive way to access information within PDF documents.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Environment Variables](#environment-variables)
- [Technical Details](#technical-details)
- [Contributing](#contributing)
  
## Project Overview

**PDFBOT** uses a combination of LangChain and large language models to convert uploaded PDF documents into an interactive chat assistant. The app provides a conversational interface where users can ask questions about the PDF content and receive relevant responses. 

## Features

- **Upload PDFs**: Drag and drop one or multiple PDF files.
- **Vectorization**: Processes the PDF content into vector embeddings using HuggingFace.
- **Interactive Chat**: Ask questions directly related to PDF content.
- **ChromaDB Integration**: Uses ChromaDB to store and retrieve vectorized document chunks for efficient querying.

## Installation

To set up PDFBOT on your local machine, follow these steps.

### Prerequisites

- [Python 3.8+](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installation/)

### Steps

1. **Clone the Repository**

   ```bash
   git clone https://github.com/amMistic/PDFBOT.git
   cd PDFBOT
   ```

2. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**

   Create a `.env` file in the project root with the following content:

   ```env
   OPENAI_API_KEY=your_openai_api_key
   groq_api_key=<your_api_key>
   HUGGINGFACEHUB_API_TOKEN=<your_huggingface_api_token>
   ```

5. **Run the Application**

   ```bash
   streamlit run app.py
   ```

6. Open your browser and navigate to `http://localhost:8501` to use PDFBOT.

## Usage

1. **Upload PDF(s)**: In the sidebar, upload your PDFs.
2. **Process PDFs**: Click the "Process" button to convert the content into vector embeddings.
3. **Chat**: Use the input box to ask questions about the uploaded PDF content.

## Project Structure

```plaintext
.
├── app.py                    # Main Streamlit app file
├── README.md                 # Documentation
├── requirements.txt          # Python dependencies
├── embeddings.py             # Embedding setup using HuggingFace
├── pdfbot.py                 # PDF processing and vectorization
├── Handle_user.py            # Handles user responses and conversation chain
├── .env                      # Environment variables (not included in repo)
└── vecDatabase/              # Directory to store ChromaDB vector databases
```

## Environment Variables

This project requires a `.env` file with the following variable:
Example:
- `OPENAI_API_KEY`: Your OpenAI API key for accessing LLMs.

## Technical Details

1. **PDF Content Extraction**: Uses `pdfplumber` to extract text from uploaded PDFs.
2. **Vectorization**: Uses `HuggingFaceEmbeddings` with `sentence-transformers/all-mpnet-base-v2` to create embedding vectors for PDF content.
3. **Database Management**: Vectorized content is stored in a local `ChromaDB` instance for fast retrieval.
4. **LLM Integration**: Uses `ChatGroq` with `Llama3-8b-8192` model for generating responses.

## Contributing

If you would like to contribute to this project, please fork the repository and create a pull request. Feel free to report issues or suggest new features.
I welcome contributions from the community! To get started:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Make your changes and commit them:
   ```bash
   git commit -m "Add a new feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Create a pull request on GitHub.
   ```bash
   git pull origin feature/your-feature-name
