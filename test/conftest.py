from fastapi.testclient import TestClient
from pytest import fixture

from app.app_factory import app


@fixture
def client():
    yield TestClient(app)
