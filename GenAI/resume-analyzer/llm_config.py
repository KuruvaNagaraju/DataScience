"""
Module to interact with a local or remote vLLM,Ollama model using REST API.

Includes:
- API authentication via Bearer Token
- Dynamic loading of environment configs
- JSON request/response handling
"""

import os
import requests
import logging
from typing import Optional
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# ----------------------------------------
# Configure Logging
# ----------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s]: %(message)s",
    handlers=[logging.FileHandler("llm_client.log"), logging.StreamHandler()]
)

# ----------------------------------------
# Constants from environment
# ----------------------------------------
VLLM_API_URL = os.getenv("VLLM_API_URL", "http://localhost:8000/v1/chat/completions")
VLLM_API_KEY = os.getenv("VLLM_API_KEY")
VLLM_MODEL_NAME = os.getenv("VLLM_MODEL_NAME") # or any other model pulled via VLLM
OLLAMA_API_URL = os.getenv("OLLAMA_API_URL", "http://localhost:11434/api/generate")
OLLAMA_LLM_MODEL_NAME = os.getenv("OLLAMA_LLM_MODEL_NAME", "granite3.3:8b")  # or any other model pulled via Ollama


def query_vllm(prompt: str) -> Optional[str]:
    """
    Queries a vLLM model with the given prompt and returns the response.

    Args:
        prompt (str): User prompt to be sent to the LLM.

    Returns:
        Optional[str]: The generated response content from the LLM,
                       or an error message if the request fails.
    """
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {VLLM_API_KEY}"
    }

    payload = {
        "model": VLLM_MODEL_NAME,
        "messages": [
            {
                "role": "user",
                "content": [{"type": "text", "text": prompt}]
            }
        ]
    }

    try:
        logging.info("Sending request to vLLM API.")
        response = requests.post(VLLM_API_URL, headers=headers, json=payload)
        response.raise_for_status()  # Raises HTTPError for bad responses

        response_json = response.json()
        result = response_json["choices"][0]["message"]["content"]
        logging.info("Received successful response from vLLM.")
        return result

    except requests.exceptions.RequestException as req_err:
        logging.error(f"RequestException: Failed to connect to vLLM - {req_err}")
    except KeyError as key_err:
        logging.error(f"KeyError in response parsing: {key_err}")
    except Exception as e:
        logging.exception(f"Unexpected error occurred: {e}")

    return "[ERROR]: Failed to get response from vLLM."


def query_ollama(prompt: str) -> Optional[str]:
    """
    Queries an Ollama model with the given prompt and returns the response.

    Args:
        prompt (str): User prompt to be sent to the LLM.

    Returns:
        Optional[str]: The generated response content from the LLM,
                       or an error message if the request fails.
    """
    payload = {
        "model": OLLAMA_LLM_MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }

    try:
        logging.info("Sending request to Ollama API.")
        response = requests.post(OLLAMA_API_URL, json=payload)
        response.raise_for_status()

        response_json = response.json()
        result = response_json.get("response", "").strip()
        logging.info("Received successful response from Ollama.")
        return result

    except requests.exceptions.RequestException as req_err:
        logging.error(f"RequestException: Failed to connect to Ollama - {req_err}")
    except KeyError as key_err:
        logging.error(f"KeyError in response parsing: {key_err}")
    except Exception as e:
        logging.exception(f"Unexpected error occurred: {e}")

    return "[ERROR]: Failed to get response from Ollama."
