"""Descarga de adjuntos guardados en uploads/."""

from __future__ import annotations

import os

from flask import Blueprint, abort, current_app, send_file

files_bp = Blueprint("files", __name__)


@files_bp.get("/files/<path:name>")
def download(name: str):
    base = current_app.config["TASKNOTES_UPLOADS"]
    path = os.path.join(base, name)
    if not os.path.isfile(path):
        abort(404)
    return send_file(path)
