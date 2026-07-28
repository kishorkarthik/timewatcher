import pytest

from timewatcher_cli import bootstrap
from timewatcher_core.repositories.sqlite_session_repository import (
    SQLiteSessionRepository,
)
from timewatcher_core.services.session_manager import SessionManager

from timewatcher_core.use_cases.start_session import StartSession
from timewatcher_core.use_cases.stop_session import StopSession
from timewatcher_core.use_cases.get_status import GetStatus
from timewatcher_core.use_cases.get_history import GetHistory


@pytest.fixture(autouse=True)
def reset_database(tmp_path):
    database_path = tmp_path / "test_timewatcher.db"

    repository = SQLiteSessionRepository(database_path)
    manager = SessionManager(repository)

    bootstrap.repository = repository
    bootstrap.manager = manager

    bootstrap.start_session = StartSession(manager)
    bootstrap.stop_session = StopSession(manager)
    bootstrap.get_status = GetStatus(manager)
    bootstrap.get_history = GetHistory(manager)