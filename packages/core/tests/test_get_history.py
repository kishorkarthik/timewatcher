from timewatcher_core.repositories.inmemory_session_repository import (
    InMemorySessionRepository,
)
from timewatcher_core.services.session_manager import SessionManager
from timewatcher_core.use_cases.get_history import GetHistory

def test_return_completed_sessions():
    repo = InMemorySessionRepository()
    manager = SessionManager(repo)

    session = manager.start("task")
    manager.stop()

    use_case = GetHistory(manager)

    history = use_case.execute()

    assert history == [session]

def test_returns_empty_list_when_no_sessions_exist():
    repo = InMemorySessionRepository()
    manager = SessionManager(repo)

    use_case = GetHistory(manager)

    assert use_case.execute() == []