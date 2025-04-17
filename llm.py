# llm.py
import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def ask_ollama(prompt: str, model: str = "phi") -> str:
    response = requests.post(OLLAMA_URL, json={
        "model": model,
        "prompt": prompt,
        "stream": False, 
        "keep-allive": 60
    })

    if response.status_code == 200:
        return response.json().get("response", "").strip()
    else:
        return f"Error: {response.status_code} - {response.text}"
