# 🤖 Streamlit Chatbot UI with External API Integration

This is a minimal and responsive chatbot UI built with **Streamlit**, which connects to an external **LLM-based API endpoint**. It supports chat history, animated message rendering, and secure key-based authorization via `.env`.

---

## 📌 Features

- 🧠 User input captured via `st.chat_input`
- 🔁 Chat history maintained across sessions
- 🧵 Sends conversation context to a custom API endpoint
- ⏱️ Simulates token streaming for user experience
- 🔐 API Key secured via `.env`
- 💬 Clean and interactive chat interface with Streamlit's new chat elements

---

## 🚀 How It Works

### 1. User inputs a message
The user enters a prompt via the Streamlit chat input.

### 2. Message sent to API
The prompt along with the previous chat history is sent as a `POST` request to the external endpoint (from `.env`).

### 3. API returns a final response
The server responds with a `final_output`, which is displayed to the user in a chunked animation to simulate streaming.

### 4. Chat history is stored
Up to the last 5 input-output pairs are stored in the session for continued conversation.

---

## ⚙️ Tech Stack

| Purpose             | Technology     |
|---------------------|----------------|
| Web UI              | Streamlit      |
| Backend Request     | Requests       |
| Environment Config  | python-dotenv  |
| Streaming Effect    | time.sleep     |

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/streamlit-endpoint-chatbot.git
cd streamlit-endpoint-chatbot
