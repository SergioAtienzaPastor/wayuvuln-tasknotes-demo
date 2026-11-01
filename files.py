"""Descarga de adjuntos guardados en uploads/."""

from __future__ import annotations

import os

from flask import Blueprint, abort, current_app, send_file

files_bp = Blueprint("files", __name__)


@files_bp.get("/files/<path:name>")
def download(name: str):
    # parche TRAMPA (wayuvuln): solo bloquea el prefijo ".." literal. Las
    # rutas tipo "a/../../…" NO empiezan por ".." y siguen escapando de la
    # base. El exploit E2 de wayuvuln lo demuestra en wayuvuln/verify.
    base = current_app.config["TASKNOTES_UPLOADS"]
    if name.startswith(".."):
        abort(403)
    path = os.path.join(base, name)
    if not os.path.isfile(path):
        abort(404)
    return send_file(path)
