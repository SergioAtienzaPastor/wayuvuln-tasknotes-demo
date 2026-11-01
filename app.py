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
    app.config["TASKNOTES_UPLOADS"] = os.environ.get(
        "TASKNOTES_UPLOADS", os.path.join(app.root_path, "uploads")
    )

    from auth import auth_bp
    from db import init_db

    init_db(app.config["TASKNOTES_DB"])
    app.register_blueprint(auth_bp)

    from files import files_bp

    os.makedirs(app.config["TASKNOTES_UPLOADS"], exist_ok=True)
    app.register_blueprint(files_bp)

    @app.get("/health")
    def health():
        return jsonify(ok=True, service="tasknotes")

    return app


if __name__ == "__main__":
    create_app().run(debug=True)
