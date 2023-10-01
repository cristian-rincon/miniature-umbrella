from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_car():
    response = client.post(
        "/cars/",
        json={"brand": "Ford", "model": "Fiesta", "year": 2001},
    )
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "brand": "Ford",
        "model": "Fiesta",
        "year": 2001,
    }