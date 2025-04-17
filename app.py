import streamlit as st
from llm import ask_ollama

st.title("🧠 Wairua ")
st.text("The Guardian of Your Knowledge")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("Ask me anything...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
   
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = ask_ollama(user_input)
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})

    st.rerun()
