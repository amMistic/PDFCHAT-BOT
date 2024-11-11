# use llama 3 model as LLM
from langchain_groq import ChatGroq 
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from dotenv import load_dotenv

# load all environment variables
load_dotenv()

def conversational_chain(vector_store):
    llm = ChatGroq(
        model_name = 'Llama3-8b-8192'
        )

    # prompt
    system_prompt = (
        "You are an intelligent assistant. Answer user queries based on the retrieved context. "
        "If the context answers the question, respond clearly. If not, admit you don't know, "
        "and suggest where to find more information. Be polite and relevant."
        "\n\nContext: {context}\n\nAnswer the user's query."
    )

    #chat prompt
    prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}"),
    ])
    
    # get the retriever
    retriever = vector_store.as_retriever()
    
    # create question answer conversation chain
    QA_chain = create_stuff_documents_chain(llm=llm, prompt=prompt)
    
    return create_retrieval_chain(retriever, QA_chain)
    
def get_response(user_query, vector_store):
    #
    responses = conversational_chain(vector_store)
    
    # 
    response = responses.invoke({
        'input': user_query
    })
    
    return response.get('answer', "Sorry!! Can't address your current query :(")