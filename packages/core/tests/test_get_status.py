from timewatcher_core.repositories.inmemory_session_repository import (
    InMemorySessionRepository,
)
from timewatcher_core.services.session_manager import SessionManager
from timewatcher_core.use_cases.get_status import GetStatus

def test_returns_active_session():
    repo = InMemorySessionRepository()
    manager = SessionManager(repo)

    session = manager.start("task")

    use_case = GetStatus(manager)

    result = use_case.execute()

    assert result is session

def test_returns_none_when_no_session_is_active():
    repo = InMemorySessionRepository()
    manager = SessionManager(repo)

    use_case = GetStatus(manager)

    assert use_case.execute() is None