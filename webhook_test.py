import requests

url = "http://localhost:5678/webhook-test/80472efe-68a4-4346-b498-b1f64cc584eb"

# Example payload
payload = {
    "event_type": "order_created",
    "timestamp": "2024-03-19T10:30:00Z",
    "data": {
        "order_id": "ORD-123456",
        "customer": {
            "id": "CUST-789",
            "name": "John Doe",
            "email": "john.doe@example.com"
        },
        "items": [
            {
                "product_id": "PROD-001",
                "name": "Widget A",
                "quantity": 2,
                "price": 29.99
            },
            {
                "product_id": "PROD-002",
                "name": "Widget B",
                "quantity": 1,
                "price": 49.99
            }
        ],
        "total_amount": 109.97
    }
}

# Headers
headers = {
    "Content-Type": "application/json",
}

# Send POST request
response = requests.post(url, json=payload, headers=headers)

# Print response
print(f"Status Code: {response.status_code}")
print(f"Response: {response.text}")