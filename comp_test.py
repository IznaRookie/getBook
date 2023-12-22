import os
import random
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "book_id" in response.json()
    assert "cover" in response.json()

def test_read_list():
    response = client.get("/list/?q=1")
    data = response.json()
    print(data)
    assert response.status_code == 200
    assert all("book_id" in item for item in response.json())
    assert all("cover" in item for item in response.json())
