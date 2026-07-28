from timewatcher_core.repositories.sqlite_session_repository import (
    SQLiteSessionRepository,
)
from timewatcher_core.models.session import Session
import sqlite3

def test_repository_can_be_created(tmp_path):
    db_path = tmp_path / "timewatcher.db"

    repository = SQLiteSessionRepository(db_path)

    assert repository is not None

def test_repository_creates_database_file(tmp_path):
    database_path = tmp_path / "timewatcher.db"

    SQLiteSessionRepository(database_path)

    assert database_path.exists()

def test_repository_creates_sessions_table(tmp_path):
    database_path = tmp_path / "timewatcher.db"

    SQLiteSessionRepository(database_path)

    connection = sqlite3.connect(database_path)

    cursor = connection.execute("""
        SELECT name
        FROM sqlite_master
        WHERE type='table'
          AND name='sessions'
    """)

    assert cursor.fetchone() is not None

def test_save_persists_session(tmp_path):
    database_path = tmp_path / "timewatcher.db"

    repository = SQLiteSessionRepository(database_path)

    session = Session.start("Implement SQLite repository")

    repository.save(session)

    # Verify by querying the database directly

def test_active_session_returns_saved_active_session(tmp_path):
    database_path = tmp_path / "timewatcher.db"

    repository = SQLiteSessionRepository(database_path)

    session = Session.start("Implement active session")

    repository.save(session)

    active = repository.active_session()

    assert active is not None
    assert active.id == session.id
    assert active.task == session.task

def test_completed_sessions_returns_saved_completed_sessions(tmp_path):
    database_path = tmp_path / "timewatcher.db"

    repository = SQLiteSessionRepository(database_path)

    session = Session.start("Implement completed sessions")
    session.stop()

    repository.save(session)

    completed = repository.completed_sessions()

    assert len(completed) == 1
    assert completed[0].id == session.id
    assert completed[0].task == session.task