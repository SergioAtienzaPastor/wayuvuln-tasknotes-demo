"""tasknotes — API mínima de notas (testbench de seguridad wayuvuln)."""

from __future__ import annotations

from flask import Flask, jsonify


def create_app() -> Flask:
    app = Flask(__name__)

    @app.get("/health")
    def health():
        return jsonify(ok=True, service="tasknotes")

    return app


if __name__ == "__main__":
    create_app().run(debug=True)
