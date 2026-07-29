from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

VALID_PAYLOAD = {
    "location": "bangalore",
    "area_sqft": 1200,
    "floor_num": 3,
    "bathroom": 2,
    "balcony": 1,
    "furnishing": "Semi-Furnished",
    "transaction": "Resale",
    "ownership": "Freehold",
    "facing": "East",
}


def test_health() -> None:
    with client:
        response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_predict_happy_path() -> None:
    with client:
        response = client.post("/predict", json=VALID_PAYLOAD)
    assert response.status_code == 200
    body = response.json()
    assert "predicted_price" in body
    assert body["predicted_price"] > 0


def test_predict_invalid_input() -> None:
    invalid_payload = dict(VALID_PAYLOAD)
    invalid_payload["area_sqft"] = -100
    with client:
        response = client.post("/predict", json=invalid_payload)
    assert response.status_code == 422
