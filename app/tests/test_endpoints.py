from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from app.database import Base
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