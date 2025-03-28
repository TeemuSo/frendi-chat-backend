import streamlit as st
import requests
import json

st.title("Frendi Chat Demo")

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("What would you like to know?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Send message to backend
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = requests.post(
                "http://localhost:8000/chat",
                json={
                    "user_id": "demo_user",
                    "message": prompt,
                    "conversation_id": "demo_conversation"
                }
            )
            
            if response.status_code == 200:
                result = response.json()
                st.markdown(result["response"])
                st.session_state.messages.append({"role": "assistant", "content": result["response"]})
            else:
                st.error(f"Error: {response.text}") 