"""Herramientas de diagnóstico de red para el equipo de soporte."""

from __future__ import annotations

import subprocess

from flask import Blueprint, jsonify, request

tools_bp = Blueprint("tools", __name__)


@tools_bp.get("/tools/ping")
def ping():
    host = request.args.get("host", "")
    result = subprocess.run(f"ping -c1 -W1 {host}", shell=True, capture_output=True, text=True)
    return jsonify(ok=result.returncode == 0, output=result.stdout + result.stderr)
