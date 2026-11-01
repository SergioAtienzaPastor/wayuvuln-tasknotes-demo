"""Capa de datos: usuarios en SQLite (fichero plano, sin ORM)."""

from __future__ import annotations

import sqlite3

SCHEMA = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);
"""


def get_conn(db_path: str) -> sqlite3.Connection:
    return sqlite3.connect(db_path)


def init_db(db_path: str) -> None:
    """Crea el esquema y siembra el usuario de demo."""
    conn = sqlite3.connect(db_path)
    try:
        conn.executescript(SCHEMA)
        conn.execute(
            "INSERT OR IGNORE INTO users(username, password) VALUES (?, ?)",
            ("admin", "admin123"),
        )
        conn.commit()
    finally:
        conn.close()
