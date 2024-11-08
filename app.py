import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage
from pdfbot import get_vector_store
from Handle_user import get_response

def main():

    # Page configurations
    st.set_page_config('PDFBOT 🤖')
    st.title('Chat with PDF 🤖')

    # session variables
    if 'visible' not in st.session_state:
        st.session_state.visible = False
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = [
        AIMessage(content='Hi! I am PDFBOT 🤖. Your Personal Blog Assistant. How can I assist you today?')
        ]

    # Add Side bar
    with st.sidebar:
        # input field for uploading pdfs
        pdfs = st.file_uploader('Drop PDF(s) here..', accept_multiple_files=True)
        
        st.warning("Processing may take time depending on the content size, please be patient.;)")
        if 'vector_store' not in st.session_state or st.session_state.vector_store is None:
            if st.button('Process'):
                with st.spinner('Processing..'):
                    st.session_state.vector_store = get_vector_store(pdfs)
                st.session_state.visible = True
    
    
    # check whether user provide any pdf(s) to chat with
    if st.session_state.visible == True:
        user_query = st.chat_input('[o_o]: Ask me anything!')
        
        if user_query:
            response = get_response(user_query, st.session_state.vector_store)
            st.session_state.chat_history.append(HumanMessage(content=user_query))
            st.session_state.chat_history.append(AIMessage(content=response))
            
            for message in st.session_state.chat_history:
                if isinstance(message, AIMessage):
                    with st.chat_message('ai'):
                        st.write(message.content)
                        
                if isinstance(message, HumanMessage):
                    with st.chat_message('human'):
                        st.write(message.content)

if __name__ == '__main__':
    main()
    
    