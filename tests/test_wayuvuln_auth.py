"""Test de regresión wayuvuln · CWE-89 · login SQLi.

ROJO en main (el bypass entra) · VERDE con el fix parametrizado.
Cualquiera puede verificarlo: ``python -m pytest tests/test_wayuvuln_auth.py``
"""

import pytest

from app import create_app


@pytest.fixture()
def client():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as c:
        yield c


def test_bypass_sqli_rechazado(client):
    r = client.post("/login", json={"username": "' OR 1=1 -- ", "password": "no-importa"})
    assert r.status_code == 401, "el bypass de inyección SQL debe ser rechazado (401)"


def test_login_valido_sigue_funcionando(client):
    r = client.post("/login", json={"username": "admin", "password": "admin123"})
    assert r.status_code == 200
    assert r.get_json()["ok"] is True
