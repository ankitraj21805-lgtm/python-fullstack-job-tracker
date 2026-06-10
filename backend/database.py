import sqlite3
from pathlib import Path
from typing import Any, Dict, List

DB_PATH = Path(__file__).resolve().parent.parent / "database.db"


def get_connection() -> sqlite3.Connection:
    """Create a SQLite connection with dictionary-style rows."""
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def initialize_database() -> None:
    """Create database tables and seed sample data when empty."""
    with get_connection() as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS applications (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                company TEXT NOT NULL,
                role TEXT NOT NULL,
                status TEXT NOT NULL,
                source TEXT NOT NULL,
                notes TEXT DEFAULT '',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """
        )
        existing_count = connection.execute(
            "SELECT COUNT(*) AS count FROM applications"
        ).fetchone()["count"]
        if existing_count == 0:
            sample_data = [
                ("Deloitte", "Frontend Developer", "Applied", "LinkedIn", "Improve React dashboard project before follow-up."),
                ("Accenture", "Junior Full Stack Developer", "Interview", "Career Page", "Prepare FastAPI and React project explanation."),
                ("Startup", "Web Developer Intern", "Saved", "Naukri", "Customize resume and portfolio before applying."),
            ]
            connection.executemany(
                """
                INSERT INTO applications (company, role, status, source, notes)
                VALUES (?, ?, ?, ?, ?)
                """,
                sample_data,
            )


def rows_to_dicts(rows: List[sqlite3.Row]) -> List[Dict[str, Any]]:
    """Convert SQLite rows into normal dictionaries."""
    return [dict(row) for row in rows]
