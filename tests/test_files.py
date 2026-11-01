"""Descarga de adjuntos legítimos."""

import pytest

from app import create_app


@pytest.fixture()
def client(tmp_path):
    uploads = tmp_path / "uploads"
    uploads.mkdir()
    (uploads / "nota.txt").write_text("hola wayuvuln", encoding="utf-8")
    app = create_app()
    app.config["TESTING"] = True
    app.config["TASKNOTES_UPLOADS"] = str(uploads)
    with app.test_client() as c:
        yield c


def test_descarga_legitima(client):
    r = client.get("/files/nota.txt")
    assert r.status_code == 200
    assert b"hola wayuvuln" in r.data


def test_fichero_inexistente_404(client):
    assert client.get("/files/no-existe.txt").status_code == 404
