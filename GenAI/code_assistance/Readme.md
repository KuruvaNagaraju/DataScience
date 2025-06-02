# SmartCodeGen - AI Code Assistant 🧠

SmartCodeGen is an AI-powered code assistant built with Streamlit and Groq's LLaMA model that can:

- ✅ Generate code in **any programming language** (e.g., Python, Java, JavaScript, C++, Go, etc.)
- 🔧 Optimize and refactor code
- 🧪 Generate unit tests using the appropriate framework
- 📚 Add docstrings or comments tailored to the language
- 🛡️ Validate code for syntax and best practices
- 🪵 Add logging statements where applicable

> 💡 If the user doesn’t specify a language, Python is assumed as the default.

---

## 🚀 How to Run

### 1. Clone the repository
```bash
git clone https://github.com/KuruvaNagaraju/DataScience.git
cd GenAI/code_assistance
```

### 2. Create and activate a virtual environment (recommended)
```bash
python -m venv codeassit_venv
source codeassit_venv/bin/activate  # Windows: codeassit_venv\Scripts\activate
```

### 3. Install dependencies:
```bash
pip install -r requirements.txt
```

### 4. Set up your environment
Create a `.env` file:
```env
GROQ_API_KEY=your_groq_api_key_here
API_URL=https://api.groq.com/openai/v1/chat/completions
MODEL_ID=llama-3.3-70b-versatile
```


### 5. Run the app:
```bash
streamlit run smartcodegen_app.py
```

### 6. 🐳 Run with Docker
```bash
docker build -t code_assistance .
docker run -p 8501:8501 --env-file .env code_assistance
```

---

## 🧠 Powered by
- [Groq API](https://console.groq.com)
- [LLaMA 3.3-70B](https://groq.com/)
- [Streamlit](https://streamlit.io)

---

Feel free to fork and enhance this AI Code Assistant! 🌍
