"""tasknotes — API mínima de notas (testbench de seguridad wayuvuln)."""

from __future__ import annotations

import os
import tempfile

from flask import Flask, jsonify


def create_app() -> Flask:
    app = Flask(__name__)
    app.config["TASKNOTES_DB"] = os.environ.get(
        "TASKNOTES_DB", os.path.join(tempfile.gettempdir(), "tasknotes.db")
    )

    from auth import auth_bp
    from db import init_db

    init_db(app.config["TASKNOTES_DB"])
    app.register_blueprint(auth_bp)

    @app.get("/health")
    def health():
        return jsonify(ok=True, service="tasknotes")

    return app


if __name__ == "__main__":
    create_app().run(debug=True)
