"""Autenticación básica por usuario/contraseña."""

from __future__ import annotations

import sqlite3

from flask import Blueprint, current_app, jsonify, request

auth_bp = Blueprint("auth", __name__)


@auth_bp.post("/login")
def login():
    username = (request.json or {}).get("username", "")
    password = (request.json or {}).get("password", "")

    conn = sqlite3.connect(current_app.config["TASKNOTES_DB"])
    # wayuvuln fix (CWE-89): consulta PARAMETRIZADA — el input jamás se
    # interpola en el SQL, por lo que ningún payload puede alterar la cláusula.
    row = conn.execute(
        "SELECT id, username FROM users WHERE username = ? AND password = ?",
        (username, password),
    ).fetchone()
    conn.close()

    if row is None:
        return jsonify(ok=False, error="credenciales inválidas"), 401
    return jsonify(ok=True, user=row[1]), 200
