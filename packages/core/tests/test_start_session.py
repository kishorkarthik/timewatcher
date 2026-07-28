from timewatcher_core.repositories.inmemory_session_repository import (InMemorySessionRepository, )

from timewatcher_core.services.session_manager import SessionManager
from timewatcher_core.use_cases.start_session import StartSession
import pytest

def test_start_session_creates_new_session():
    repo = InMemorySessionRepository()
    manager = SessionManager(repo)
    use_case = StartSession(manager)

    session = use_case.execute("Write documentation")

    assert session.task == "Write documentation"
    assert session.is_active

def test_start_session_raises_when_session_is_already_active():
    repo = InMemorySessionRepository()
    manager = SessionManager(repo)
    use_case = StartSession(manager)

    use_case.execute("Task 1")

    with pytest.raises(RuntimeError):
        use_case.execute("Task 2")