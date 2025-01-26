# Project Overview

This project is a multi-service application using Docker Compose. It includes services for `n8n`, `Postgres`, `Ollama`, and `Ollama Web UI`.

## Services

### n8n
- **Image**: `docker.n8n.io/n8nio/n8n`
- **Port**: `5678`
- **Environment Variables**:
  - `N8N_HOST`
  - `N8N_PORT`
  - `N8N_PROTOCOL`
  - `DB_TYPE`
  - `DB_POSTGRESDB_HOST`
  - `DB_POSTGRESDB_DATABASE`
  - `DB_POSTGRESDB_USER`
  - `DB_POSTGRESDB_PASSWORD`
- **Volumes**: `n8n_data`
- **Depends on**: `postgres`

### Postgres
- **Image**: `postgres:15-alpine`
- **Port**: `5432`
- **Environment Variables**:
  - `POSTGRES_USER`
  - `POSTGRES_PASSWORD`
  - `POSTGRES_DB`
  - `POSTGRES_NON_ROOT_USER`
- **Volumes**: `postgres_data`

### Ollama
- **Image**: `ollama/ollama:latest`
- **Port**: `11434`
- **Volumes**: `ollama_data`

### Ollama Web UI
- **Image**: `ghcr.io/ollama-webui/ollama-webui:main`
- **Port**: `3000`
- **Environment Variables**:
  - `OLLAMA_API_BASE_URL`
- **Depends on**: `ollama`

## Testing

A test script `test_ollama.py` is provided to test the Ollama service. It sends a POST request to the Ollama API to generate a response for the prompt "What is the capital of France?".

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
if name == "main":
test_ollama()
```

Run the test script:

```bash
python test_ollama.py
```

## Volumes

- `n8n_data`
- `postgres_data`
- `ollama_data`

## Getting Started

1. Ensure Docker and Docker Compose are installed on your machine.
2. Clone the repository.
3. Run `docker-compose up` to start all services.
4. Access the services via their respective ports.
