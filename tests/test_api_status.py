import requests

def test_api_status():
    response = requests.get("https://api.github.com")

    assert response.status_code == 200
