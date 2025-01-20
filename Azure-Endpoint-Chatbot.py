#endpoint  connected chatbot
import streamlit as st 
import requests  
import time  # For simulating delay
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
#Calling Credential from .env
API_ENDPOINT = os.getenv("API_ENDPOINT")
API_KEY = os.getenv("API_KEY")

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

if "chat_history" not in st.session_state:
    st.session_state.chat_history = [] 


# Display previous chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Prepare the request body
    request_body = {
        "chat_input": prompt,
        "chat_history": st.session_state.chat_history  
    }

    # Send request to the API endpoint
    response = requests.post(API_ENDPOINT, json=request_body, headers=headers)

    if response.status_code == 200:
        
        response_json = response.json()
        full_response = response_json.get("final_output", "Sorry, I couldn't get a response.")

        # Display the assistant's response with chunking
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            current_output = ""

            # Simulate chunk streaming (replace with true streaming if supported by your API)
            for i in range(0, len(full_response), 50):  # Chunk size = 50 characters
                chunk = full_response[i:i + 50]
                current_output += chunk
                message_placeholder.markdown(current_output + "▌")  # Add cursor (▌)
                time.sleep(0.1)  # Simulate delay between chunks

            message_placeholder.markdown(current_output)  # Finalize response without cursor

        # Store the input-output pair in chat history
        st.session_state.chat_history.append({
            "inputs": {"chat_input": prompt},
            "outputs": {"final_output": full_response}
        })

        # Keep only the last 5 chat history pairs
        if len(st.session_state.chat_history) > 5:
            st.session_state.chat_history.pop(0)  

    else:
        
        full_response = "Error: Unable to get a response from the model."
        with st.chat_message("assistant"):
            st.markdown(full_response)

    # Save response in session state
    st.session_state.messages.append({"role": "assistant", "content": full_response})
