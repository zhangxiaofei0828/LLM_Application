import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_chatbot_response():
    response = client.post("/chat", json={"message": "Hello"})
    assert response.status_code == 200
    assert "response" in response.json()

def test_chatbot_invalid_input():
    response = client.post("/chat", json={"message": ""})
    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid input"}