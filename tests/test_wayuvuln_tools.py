"""Test de regresión wayuvuln · CWE-78 · inyección de comandos en /tools/ping.

ROJO en main (`; comando` se ejecuta) · VERDE con el fix allowlist+sin shell.
"""

import pytest

from app import create_app


@pytest.fixture()
def client():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as c:
        yield c


def test_inyeccion_de_comando_bloqueada(client):
    r = client.get("/tools/ping", query_string={"host": "127.0.0.1; id"})
    body = r.get_data(as_text=True)
    assert "uid=" not in body, "el comando inyectado NO debe ejecutarse"
    assert r.status_code in (200, 400)


def test_host_valido_aceptado(client):
    r = client.get("/tools/ping", query_string={"host": "127.0.0.1"})
    assert r.status_code == 200
