from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "message": "Frendi Chat API is running"}

def test_create_message():
    response = client.post(
        "/api/messages",
        json={"content": "Test message"}
    )
    assert response.status_code == 200
    assert response.json()["content"] == "Test message"
    assert "id" in response.json()
    assert "timestamp" in response.json()

def test_get_messages():
    # First create a message
    client.post("/api/messages", json={"content": "Get messages test"})
    
    # Then get all messages
    response = client.get("/api/messages")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    
    # Check if our message is in the list
    messages = response.json()
    assert any(msg["content"] == "Get messages test" for msg in messages)

def test_get_message_by_id():
    # First create a message
    response = client.post("/api/messages", json={"content": "Get by ID test"})
    message_id = response.json()["id"]
    
    # Then get it by ID
    response = client.get(f"/api/messages/{message_id}")
    assert response.status_code == 200
    assert response.json()["id"] == message_id
    assert response.json()["content"] == "Get by ID test"

def test_get_message_not_found():
    response = client.get("/api/messages/999999")
    assert response.status_code == 404 