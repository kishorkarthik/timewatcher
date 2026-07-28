from pathlib import Path
from timewatcher_core.repositories.sqlite_session_repository import (
    SQLiteSessionRepository,
)
from timewatcher_core.services.session_manager import SessionManager

from timewatcher_core.use_cases.start_session import StartSession
from timewatcher_core.use_cases.stop_session import StopSession
from timewatcher_core.use_cases.get_status import GetStatus
from timewatcher_core.use_cases.get_history import GetHistory

database_path = Path.cwd() / "timewatcher.db"

repository = SQLiteSessionRepository(database_path)
manager = SessionManager(repository)

start_session = StartSession(manager)
stop_session = StopSession(manager)
get_status = GetStatus(manager)
get_history = GetHistory(manager)