# VLLM Setup on CPU

This guide walks you through setting up and running the [vLLM](https://github.com/vllm-project/vllm) project on a CPU-only environment using the `ibm-granite/granite-3.0-2b-instruct` model.

---

## 🚀 Installation Steps

### 1. Clone the vLLM repository

```bash
git clone https://github.com/vllm-project/vllm.git
cd vllm
```

### 2. Install CPU requirements

```bash
pip install -r requirements/cpu.txt
```

### 3. Install vLLM in editable mode

```bash
pip install -e .
```

---

## 🔐 Generate API Key

You can use the command below to generate a secure token for API authentication.

```bash
openssl rand -base64 32
```

Save this token safely and replace `<TOKEN>` with it in the steps below.

---

## 🧠 Start the vLLM Server

Run the model server using the command below. Make sure to replace `<TOKEN>` with your generated token.

```bash
vllm serve ibm-granite/granite-3.0-2b-instruct \
  --max-model-len 4096 \
  --port 8000 \
  --seed 42 \
  --api-key <TOKEN>
```

---

## ✅ Verify Server Status

To check the models available on your vLLM server:

```bash
curl http://localhost:8000/v1/models \
-H 'Authorization: Bearer <TOKEN>'
```

---

## 💬 Run a Chat Completion Request

You can test your setup with a simple question like this:

```bash
curl -X POST 'http://localhost:8000/v1/chat/completions' \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer <TOKEN>' \
-d '{
  "model": "ibm-granite/granite-3.0-2b-instruct",
  "messages": [
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "What is the color of rainbow?"}
      ]
    }
  ]
}'
```

---

## 📌 Notes

- This setup is for **CPU-only environments**. Running larger models on CPU can be slow; for production or intensive use, consider using a GPU-enabled environment.
- If you're using `.env` files to store credentials, load the token using Python's `os.getenv()` in your apps.
- Ensure ports and firewalls are open if accessing the server remotely.

---

## 🧾 Resources

- vLLM GitHub: [https://github.com/vllm-project/vllm](https://github.com/vllm-project/vllm)
- IBM Granite Model: [ibm-granite on Hugging Face](https://huggingface.co/ibm-granite)
