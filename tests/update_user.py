import requests
from utils.config import BASE_URL
from utils.client import get

def test_update_user():
    url = f"{BASE_URL}/users"
    payload = {
        "name": "Jael Updated",
        "username": "jael_updated"
    }

    response = get("/users")

    # Status code validation
    assert response.status_code == 200

    data = response.json()

    # Validate updated data
    assert data["name"] == "Jael Updated"
    assert data["username"] == "jael_updated"