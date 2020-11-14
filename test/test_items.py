from fastapi.testclient import TestClient


def test_items(client: TestClient):
    response = client.get("/items")
    assert response.status_code == 200
    assert response.json()["count"] == 9


def test_missing_id(client: TestClient):
    response = client.get("items/0")
    assert response.status_code == 404


def test_item(client: TestClient):
    response = client.get("items/1")
    assert response.status_code == 200
