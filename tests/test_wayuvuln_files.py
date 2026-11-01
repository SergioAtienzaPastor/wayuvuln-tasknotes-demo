"""Test de regresión wayuvuln · CWE-22 · path traversal en /files.

ROJO en main (las rutas escapan de uploads/) · VERDE con el fix realpath.
El objetivo es un secret vecino de uploads/ (determinista, independiente de
la profundidad de directorios).
"""

import pytest

from app import create_app

SECRET_MARKER = "WAYUVULN-SECRET-7f3a"


@pytest.fixture()
def client(tmp_path):
    uploads = tmp_path / "uploads"
    (uploads / "docs").mkdir(parents=True)
    (uploads / "nota.txt").write_text("hola wayuvuln", encoding="utf-8")
    secret = tmp_path / "secret"
    secret.mkdir()
    (secret / "secret.txt").write_text(SECRET_MARKER, encoding="utf-8")
    app = create_app()
    app.config["TESTING"] = True
    app.config["TASKNOTES_UPLOADS"] = str(uploads)
    with app.test_client() as c:
        yield c


@pytest.mark.parametrize(
    "url",
    [
        "/files/..%2Fsecret%2Fsecret.txt",
        "/files/docs%2F..%2F..%2Fsecret%2Fsecret.txt",  # no empieza por ".."
        "/files/..%2fsecret%2fsecret.txt",
    ],
)
def test_traversal_bloqueado(client, url):
    r = client.get(url)
    assert r.status_code == 404, f"el traversal debe dar 404, no {r.status_code}: {url}"
    assert SECRET_MARKER.encode() not in r.data


def test_descarga_legitima_sigue_funcionando(client):
    r = client.get("/files/nota.txt")
    assert r.status_code == 200
    assert b"hola wayuvuln" in r.data
