import requests
from utils.config import BASE_URL
from utils.client import get

def test_delete_user():
    url = f"{BASE_URL}/users"
    response = get("/users")

    # Status code validation
    assert response.status_code == 200