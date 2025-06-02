"""
SmartCodeGen - AI Code Assistant (Streamlit + Groq API)

This Streamlit app allows users to interact with an LLM (Groq’s LLaMA model)
to generate, optimize, validate, document, log, and test Python code using natural language.
"""

import os
import logging
import requests
import streamlit as st
from dotenv import load_dotenv

# =======================
# Configuration & Setup
# =======================

# Load environment variables from .env file
load_dotenv()

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] - %(message)s"
)

# Retrieve environment variables securely
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
API_URL = os.getenv("API_URL")
MODEL_ID = os.getenv("MODEL_ID")

# Validate essential configs
if not GROQ_API_KEY or not API_URL or not MODEL_ID:
    st.error("❌ Environment variables GROQ_API_KEY, API_URL, or MODEL_ID are missing in your .env file.")
    st.stop()

# Set API headers
HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {GROQ_API_KEY}"
}

# LLM system prompt instructing capabilities
SYSTEM_PROMPT = (
    "You are an intelligent AI assistant that helps with software development across all programming languages.\n"
    "The user may or may not specify the programming language in their request.\n"
    "If a language is mentioned (like Python, JavaScript, Java, C++, etc.), provide the solution in that language.\n"
    "If no language is mentioned, assume the default language is Python.\n"
    "Based on the user's input, you can:\n"
    "- Generate new code\n"
    "- Optimize or refactor existing code\n"
    "- Add logging statements\n"
    "- Generate unit test cases using appropriate testing frameworks\n"
    "- Add detailed docstrings or comments appropriate to the language\n"
    "- Validate the code for syntax, performance, or best practices\n"
    "Your response should be concise, relevant, and properly formatted for readability."
)


# =======================
# Streamlit UI Setup
# =======================

st.set_page_config(page_title="SmartCodeGen - AI Code Assistant", page_icon="🤖")
st.title("🤖 SmartCodeGen - AI Code Assistant")

# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": SYSTEM_PROMPT}
    ]

# Display past conversation (excluding system prompt)
for msg in st.session_state.messages[1:]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input box for user query
user_query = st.chat_input("Ask me to generate, optimize, document, test, or validate Python code")

# =======================
# Handle User Query
# =======================

if user_query:
    # Log user query
    logging.info("User input: %s", user_query)

    # Append user message to session state
    st.session_state.messages.append({"role": "user", "content": user_query})

    with st.chat_message("user"):
        st.markdown(user_query)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                # Prepare payload to send to Groq LLM
                payload = {
                    "model": MODEL_ID,
                    "messages": st.session_state.messages
                }

                # Send request to LLM
                response = requests.post(API_URL, headers=HEADERS, json=payload)
                response.raise_for_status()

                # Extract response
                reply = response.json()["choices"][0]["message"]["content"]
                logging.info("LLM response received.")

            except requests.exceptions.RequestException as e:
                # Handle API request errors
                reply = f"❌ API Request Error: {str(e)}"
                logging.error("API request failed: %s", str(e))

            except Exception as e:
                # Handle generic errors
                reply = f"❌ Unexpected Error: {str(e)}"
                logging.exception("Unexpected error occurred.")

            # Show reply in the chat and save it
            st.markdown(reply)
            st.session_state.messages.append({"role": "assistant", "content": reply})