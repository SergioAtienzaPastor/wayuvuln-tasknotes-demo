"""Descarga de adjuntos guardados en uploads/."""

from __future__ import annotations

import os

from flask import Blueprint, abort, current_app, send_file

files_bp = Blueprint("files", __name__)


@files_bp.get("/files/<path:name>")
def download(name: str):
    # wayuvuln fix (CWE-22): canonicalizar y confinar a uploads/. realpath
    # resuelve TODOS los ../ (también los codificados %2e%2e) antes de mirar
    # si el fichero existe: si la ruta escapa de la base, no se sirve.
    base = os.path.realpath(current_app.config["TASKNOTES_UPLOADS"])
    path = os.path.realpath(os.path.join(base, name))
    if os.path.commonpath([base, path]) != base or not os.path.isfile(path):
        abort(404)
    return send_file(path)
