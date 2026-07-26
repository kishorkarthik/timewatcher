import pytest

from timewatcher_core.repositories.inmemory_session_repository import (
    InMemorySessionRepository,
)
from timewatcher_core.services.session_manager import SessionManager
from timewatcher_core.use_cases.stop_session import StopSession

def test_stop_session_completes_active_session():
    repo = InMemorySessionRepository()
    manager = SessionManager(repo)

    manager.start("stop session")

    use_case = StopSession(manager)

    session = use_case.execute()

    assert not session.is_active

def test_stop_session_raises_when_no_session_is_active():
    repo = InMemorySessionRepository()
    manager = SessionManager(repo)

    use_case = StopSession(manager)

    with pytest.raises(RuntimeError):
        use_case.execute()