"""Login válido / inválido."""

import pytest

from app import create_app


@pytest.fixture()
def client():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as c:
        yield c


def test_login_valido(client):
    r = client.post("/login", json={"username": "admin", "password": "admin123"})
    assert r.status_code == 200
    assert r.get_json()["ok"] is True


def test_login_invalido(client):
    r = client.post("/login", json={"username": "admin", "password": "mala"})
    assert r.status_code == 401
