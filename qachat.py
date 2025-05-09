from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Load Gemini Pro model and get response

model = genai.GenerativeModel("gemini-2.0-flash")
chat = model.start_chat(history=[])

def get_gimini_response(question):
    response = chat.send_message(question, stream=True)                # Get the access of all the streaming data
    return response

st.set_page_config(page_title="Gemini Chat", page_icon="🤖")
st.header("Gemini LLM aplication")

# Initializing Session state if doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

input = st.text_input("Input:", key="input")
submit = st.button("Ask Gemini")

if submit and input:
    response = get_gimini_response(input)
    # Add user query and response to session chat history
    st.session_state['chat_history'].append(("You", input))
    st.subheader("The response is")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot", chunk.text))

st.subheader("Chat History")

for role, text in st.session_state['chat_history']:
    st.write(f"{role}: {text}")
