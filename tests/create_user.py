import requests
from utils.config import BASE_URL
from utils.client import get

def test_create_user():
    url = f"{BASE_URL}/users"
    payload = {
        "name": "Jael",
        "username": "jael_b",
        "email": "jael@test.com"
    }

    response = get("/users")

    # Status code validation
    assert response.status_code == 201

    data = response.json()

    # Validate response data
    assert data["name"] == "Jael"
    assert data["username"] == "jael_b"