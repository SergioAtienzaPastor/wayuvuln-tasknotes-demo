"""Herramientas de diagnóstico de red para el equipo de soporte."""

from __future__ import annotations

import re
import subprocess

from flask import Blueprint, jsonify, request

tools_bp = Blueprint("tools", __name__)


@tools_bp.get("/tools/ping")
def ping():
    # wayuvuln fix (CWE-78): allowlist estricta del host + ejecución SIN
    # shell (lista de argumentos). ";" ya no puede encadenar comandos porque
    # el valor entero se valida carácter a carácter.
    host = request.args.get("host", "")
    if not re.fullmatch(r"[A-Za-z0-9._-]+", host):
        return jsonify(ok=False, error="host inválido"), 400
    result = subprocess.run(["ping", "-c1", "-W1", host], capture_output=True, text=True)
    return jsonify(ok=result.returncode == 0, output=result.stdout + result.stderr)
