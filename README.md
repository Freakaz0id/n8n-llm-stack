# Project Overview

This project is a multi-service application using Docker Compose. It includes services for `n8n`, `Postgres`, `Ollama`, and `Ollama Web UI`.


## Getting Started

1. Ensure Docker and Docker Compose are installed on your machine.
2. Clone the repository.
3. Create a `.env` file in the root of the project with the following variables:
    - N8N_HOST=localhost  # or your domain name
    - N8N_PROTOCOL=http  # or https
    - POSTGRES_PASSWORD=xxxxxxxxxxxxxxx  # Database password
4. Run `docker-compose up` to start all services.
5. Access n8n at http://localhost:5678/
6. Access ollama-webui at http://localhost:3000/


## Using the Ollama API

A test script `test_ollama.py` is provided to test the Ollama service. It sends a POST request to the Ollama API to generate a response for the prompt "What is the capital of France?".
Make sure to the model in question is installed in the Ollama instance. E.g. run `ollama pull tinyllama` in the ollama container shell.

```python
import requests
def test_ollama():
    response = requests.post('http://localhost:11434/api/generate',
    json={
        "model": "tinyllama",
        "prompt": "What is the capital of France?"
    }
)

print(response.text)

if __name__ == "__main__":
    test_ollama()
```

Run the test script:

```bash
python test_ollama.py
```
