import requests
from utils.config import BASE_URL
from utils.client import get

def test_get_users():
    url = f"{BASE_URL}/users"
    
    response = get("/users")
    # Status code validation
    assert response.status_code == 200

    data = response.json()

    # Validate response is a list
    assert isinstance(data, list)

    # Check at least one user exists
    assert len(data) > 0