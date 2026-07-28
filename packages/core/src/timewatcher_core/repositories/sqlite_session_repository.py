from timewatcher_core.repositories.session_repository import SessionRepository
from timewatcher_core.models.session import Session
from pathlib import Path
import sqlite3
from datetime import datetime
from uuid import UUID

class SQLiteSessionRepository(SessionRepository):
    def __init__(self, database_path: Path):
        self._database_path = database_path
        self._connection = sqlite3.connect(database_path)
        self._connection.execute("""
        CREATE TABLE IF NOT EXISTS sessions (
            id TEXT PRIMARY KEY,
            task TEXT NOT NULL,
            start_time TEXT NOT NULL,
            end_time TEXT,
            is_active INTEGER NOT NULL
        )
        """)

        self._connection.commit()

    def save(self, session: Session) -> None:
        self._connection.execute(
            """
            INSERT INTO sessions (
               id,
               task,
               start_time,
               end_time,
               is_active
            )
            VALUES (?, ?, ?, ?, ?)
            ON CONFLICT(id)
            DO UPDATE SET
                task = excluded.task,
                start_time = excluded.start_time,
                end_time = excluded.end_time,
                is_active = excluded.is_active
            """,
            (
               str(session.id),
               session.task,
               session.start_time.isoformat(),
               session.end_time.isoformat() if session.end_time else None,
               int(session.is_active),
            ),
       )

        self._connection.commit()

    def active_session(self) -> Session | None:
        cursor = self._connection.execute(
            """
            SELECT id, task, start_time, end_time
            FROM sessions
            WHERE is_active = 1
            LIMIT 1
            """
)

        row = cursor.fetchone()
        if row is None:           
            return None

        return Session(
            id=UUID(row[0]),
            task=row[1],
            start_time=datetime.fromisoformat(row[2]),
            end_time=datetime.fromisoformat(row[3]) if row[3] else None,
        )

    def completed_sessions(self) -> list[Session]:
        cursor = self._connection.execute(
            """
            SELECT id, task, start_time, end_time
            FROM sessions
            WHERE is_active = 0
            ORDER BY start_time
            """
        )

        rows = cursor.fetchall()

        return [
            Session(
                id=UUID(row[0]),
                task=row[1],
                start_time=datetime.fromisoformat(row[2]),
                end_time=datetime.fromisoformat(row[3]) if row[3] else None,
            )
            for row in rows
        ]
