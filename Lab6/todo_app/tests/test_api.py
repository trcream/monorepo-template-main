from fastapi import FastAPI
import pytest
import json

# TestClient can help us with response testing
from fastapi.testclient import TestClient

from src.main import app

# python3 -m pytest tests/
# python3 -m pytest --cov=src --cov-report=html tests/


# Create an instance of the TestClient class
client = TestClient(app)

def test_get_api():
    response = client.get("/api")
    assert response.status_code == 200
    assert response.json() == {"msg": "hello_world"}

# Testing the get request with path parameters
def test_get_apiV2():
    response = client.get("/books/Harry%20Potter")
    assert response.status_code == 200
    assert response.json() == {"msg": "Harry Potter"}

# Testing the request with query parameters
def test_get_apiV3():
    response = client.get("/books/?title=Harry%20Potter")
    assert response.status_code == 200
    assert response.json() == {"msg": "Harry Potter"}

def test_get_apiV4():
    response = client.get("/books/main_actor/?actor=Harry")
    assert response.status_code == 200
    assert response.json() == {"msg": "main_actor", "actor": "Harry"}

def test_post_api():
    json_payload = {
        "title": "Harry Potter",
        "author": "J.K Rowling",
        "category": "fiction"
    }
    # json=json_payload is the body of the request
    response = client.post("/books/create_book", json=json_payload)
    assert response.status_code == 200
    assert response.json() == {"msg": json_payload}

def test_put_api():
    json_payload = {
        "title": "Trenton Potter",
        "author": "J.K Creamer",
        "category": "non-fiction"
    }
    response = client.put("/books/update_book",json = json_payload)
    assert response.status_code == 200
    assert response.json() == {"msg": json_payload}

def test_delete_api():
    book_to_delete = {
        "title": "Trenton Potter",
        "author": "J.K Creamer",
        "category": "non-fiction"
    }
    response = client.delete("/books/delete_book",params=book_to_delete)
    assert response.status_code == 200