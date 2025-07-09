# 💡 Technical Support AI Assistant

A smart, AI-powered technical support assistant built with **LangChain**, **FAISS**, **Groq LLM APIs**, and **Streamlit**.  
This system enables real-time technical issue resolution by retrieving relevant knowledge base documents and generating contextual answers via an advanced AI agent.

---

## 📊 Features

- 🚀 **FastAPI Backend** for AI query processing  
- 🎨 **Streamlit Custom Frontend UI** with unique animated neon theme  
- 📚 **Knowledge Base Search** via FAISS vector similarity  
- 🧠 **Groq API** integration for LLM-powered answers  
- 📝 **Custom Error Detection and Correction** module  
- 📈 **MLflow experiment tracking** for AI query logs, performance metrics, and response artifacts  
- 🖥️ Live **chat history**, **agent avatar**, and **real-time system clock**

---
## ScreenShot

![image alt]()
---

## 🖥️ Architecture Overview

```plaintext
+------------+       +------------+        +--------------+
|  User Input| -----> | Streamlit  | -----> | FastAPI Backend|
+------------+       +------------+        +--------------+
                                                          |
                                                          v
                                                   +------------+
                                                   | FAISS + KB |
                                                   +------------+
                                                          |
                                                          v
                                                  +---------------+
                                                  | Groq LLM Model |
                                                  +---------------+
                                                          |
                                                          v
                                                   AI Response
```
⚙️ Tech Stack
🐍 Python 3.11

📚 LangChain, LangChain Community, LangChain Groq

⚡ FastAPI + Uvicorn

🎨 Streamlit with custom CSS

🔍 FAISS (vector similarity search)

📄 Groq API for LLM inference

🐳 Docker containerization

---
```
technical_support_ai/
├── api/
│   └── main.py               # FastAPI backend
├── config/
│   └── config.yaml           # Config settings
├── knowledge_base/
│   └── *.md                  # Markdown knowledge base documents
├── src/
│   ├── agent.py              # AI agent and MLflow integration
│   ├── embeddings.py         # Groq embedding calls
│   ├── error_detection.py    # Error detection logic
│   ├── knowledge_base.py     # FAISS retriever logic
│   ├── mcp_tools.py          # System check utilities
│   ├── utils.py              # Config loader
│   └── vector_store.py       # FAISS vector index builder
├── ui/
│   └── app.py                # Custom Streamlit UI
├── Dockerfile                # Docker build config
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```
---
##📦 Setup & Installation
##1️⃣ Clone the repository:

```

git clone https://github.com/yourname/technical_support_ai.git
cd technical_support_ai
```
---
##2️⃣ Install dependencies:
```

pip install -r requirements.txt
```
---
##3️⃣ Update your config/config.yaml with your Groq API Key and paths.

---

##4️⃣ Build FAISS vector store:

```

python -m src.vector_store

```
---
## 🚀 Run the Application
Start FastAPI backend:

```
uvicorn api.main:app --reload
```
---
## Start Streamlit frontend:
```
streamlit run ui/app.py
Visit:

http://localhost:8000/docs → FastAPI Swagger UI

http://localhost:8501/ → Custom Streamlit AI Dashboard
```
---
## 👨‍💻 Author
Abel Priyakumar P— 2025
Connect: [LinkedIn](https://www.linkedin.com/in/abel-priyakumar-p/) | Email:abelpriyakumar@gmail.com
