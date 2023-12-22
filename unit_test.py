import os
import random
from unittest import mock
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

@mock.patch('main.requests.get')
def test_read_root(mock_get):
    mock_get.return_value.json.return_value = {"book_id": "Mocked Book"}
    response = client.get("/")
    assert response.status_code == 200
    assert "book_id" in response.json()


@mock.patch('main.requests.get')
def test_read_list(mock_get):
    mock_get.return_value.json.return_value = {"book_id": "Mocked Book"}
    response = client.get("/list/?q=1")
    assert response.status_code == 200
    assert all("book_id" in item for item in response.json())