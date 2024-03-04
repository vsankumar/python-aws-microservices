from fastapi.testclient import TestClient
from main import app


client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Wikipedia API.  Call /search or /wiki"}


def test_read_phrase():
    response = client.get("/phrase/Sachin Tendulkar")
    assert response.status_code == 200
    assert response.json() == {
        "result": [
            "sachin ramesh tendulkar",
            "[ sətɕin teːɳɖulkəɾ ]",
            "april",
            "international cricketer",
            "indian national team",
        ]
    }
