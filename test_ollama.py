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