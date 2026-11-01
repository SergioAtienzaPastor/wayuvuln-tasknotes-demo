"""Ping de diagnóstico (happy path)."""

import pytest

from app import create_app


@pytest.fixture()
def client():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as c:
        yield c


def test_ping_responde(client):
    r = client.get("/tools/ping", query_string={"host": "127.0.0.1"})
    assert r.status_code == 200
    assert r.get_json()["ok"] in (True, False)  # depende de ping en el host
