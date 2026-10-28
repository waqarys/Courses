from fastapi.testclient import TestClient
from book_app import app
client = TestClient(app)
def test_health_endpoint():
    r = client.get("/health"); assert r.status_code == 200 and r.json()["status"] == "healthy"
def test_chat_with_valid_input():
    r = client.post("/chat", json={"message": "Say 'test' and nothing else."}); assert r.status_code == 200; assert "response" in r.json() and "latency_ms" in r.json()
def test_chat_with_empty_input():
    assert client.post("/chat", json={"message": ""}).status_code == 422
def test_chat_with_long_input():
    r = client.post("/chat", json={"message": "x"*10000}); assert r.status_code == 400 and "too long" in r.json()["detail"].lower()
def test_false_positive_fact_as():
    r = client.post("/chat", json={"message": "In fact as a beginner, how do I learn Python?"}); print(r.status_code, r.json()); assert r.status_code == 200
def test_rate_limit_21st():
    codes=[client.post("/chat", json={"message": "x"*5000}).status_code for _ in range(21)]; print(codes[-3:]); assert 429 in codes
