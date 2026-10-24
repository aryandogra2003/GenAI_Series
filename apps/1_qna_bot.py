from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
import streamlit as st

llm=ChatGroq(model='openai/gpt-oss-20b')

st.title("QnA Bot with LangChain and Groq")
st.markdown("This is a simple QnA bot built using LangChain and Groq. Type your question below and press Enter to get an answer.")

#store older messages in session storage 
if "messages" not in st.session_state:
    st.session_state.messages=[]

for message in st.session_state.messages:
    role=message["role"]
    content=message["content"]
    st.chat_message(role).markdown(content)

query = st.chat_input("Ask anything...")
if query:
    st.session_state.messages.append({"role":"User","content":query})
    st.chat_message("user").markdown(query)

    res=llm.invoke(query)
    
    st.chat_message("ai").markdown(res.content)
    st.session_state.messages.append({"role":"AI","content":res.content})