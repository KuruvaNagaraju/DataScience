# 🧠 Ollama Setup for IBM Granite 3.0 2B Instruct Model

This guide walks you through setting up [Ollama](https://ollama.com) and running the `ibm-granite/granite-3.0-2b-instruct` model locally for LLM inference via CLI, Python, or `curl`.

---

## 📦 What is Ollama?

Ollama is a lightweight runtime for running open-source language models on your local machine with a REST API.

---

## ✅ Prerequisites

- **OS**: macOS, Linux, or Windows (WSL)
- **Docker**: Optional (for isolation)
- **Python**: Optional (for scripting)
- **curl**: For terminal-based testing

---

## 🔧 Step-by-Step Installation

### 1. Install Ollama

#### macOS:

```bash
brew install ollama
```

#### Linux:

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

#### Windows:

Download from: [https://ollama.com/download](https://ollama.com/download)

---

### 2. Start Ollama

```bash
ollama serve
```

This starts a local REST server at `http://localhost:11434`.

---

### 3. Pull IBM Granite Model (if available)

```bash
ollama pull ibm/granite-3b-instruct
```

> ⚠️ If the model isn’t available by default, use a custom Modelfile (see next step).

---

## 🧾 Optional: Use a Custom Modelfile

If needed, create a file named `Modelfile`:

```dockerfile
FROM hf://ibm-granite/granite-3.0-2b-instruct
```

Then build and run the model:

```bash
ollama create granite-3b-instruct -f Modelfile
ollama run granite-3b-instruct
```

---

## 💬 Example Prompt (CLI)

```bash
ollama run granite-3b-instruct
```

Type your prompt, e.g.:

```
What are the benefits of using local LLMs?
```

---

## 🌐 cURL API Example (REST)

After starting `ollama serve`, send a request using `curl`:

```bash
curl http://localhost:11434/api/generate \
  -d '{
    "model": "granite-3b-instruct",
    "prompt": "Explain what a data engineer does.",
    "stream": false
  }'
```

### ✅ Sample Output:

```json
{
  "response": "A data engineer builds and maintains systems that allow for the collection, storage, and analysis of data..."
}
```

---

## 🧪 Python API (Optional)

```python
import requests

response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "granite-3b-instruct",
        "prompt": "Summarize what a Machine Learning Engineer does.",
        "stream": False
    }
)

print(response.json()['response'])
```

---

## 📁 Manage Local Models

```bash
ollama list          # List all local models
ollama run <model>   # Run a model
ollama rm <model>    # Remove a model
```

Models are stored at `~/.ollama` by default.

---

## 🔒 Security Notes

- Ollama has **no authentication** by default.
- For secure use:
  - Wrap behind a proxy (e.g., NGINX with Basic Auth)
  - Bind `ollama serve` to `127.0.0.1` only (default)

---

## 📚 References

- 🔗 Ollama: [https://ollama.com](https://ollama.com)
- 🧠 IBM Granite HF: [https://huggingface.co/ibm-granite](https://huggingface.co/ibm-granite)
- 🧪 API Docs: [https://ollama.com/library](https://ollama.com/library)

---

## ✅ Summary

Ollama + IBM Granite gives you an offline, fast, local inference engine with a clean API. Use it for chatbots, summarizers, resume parsers, and other GenAI tasks without needing the cloud.

