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
    query = f"SELECT id, username FROM users WHERE username = '{username}' AND password = '{password}'"
    row = conn.execute(query).fetchone()
    conn.close()

    if row is None:
        return jsonify(ok=False, error="credenciales inválidas"), 401
    return jsonify(ok=True, user=row[1]), 200
