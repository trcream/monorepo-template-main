from fastapi import FastAPI
import pytest
import json

# TestClient can help us with response testing
from fastapi.testclient import TestClient

from src.main import app

#python -m pytest tests/

# Create an instance of the TestClient class
client = TestClient(app)

def test_get_api():
    print("Test")
    response = client.get("/api")
    assert response.status_code == 200
    assert response.json() == {"msg": "hello_world"}