import pytest
from timewatcher_core.services.session_manager import SessionManager
from timewatcher_core.models import Session

def test_new_manager_has_no_active_session():
    manager = SessionManager()

    assert manager.current_session() is None

def test_start_an_active_session():
    manager = SessionManager()

    session = manager.start("start active session")
    
    assert isinstance(session, Session)
    assert manager.current_session() is session
    assert session.task == "start active session"
    assert session.is_active

def test_cannot_start_second_active_session():
    manager = SessionManager()

    manager.start("Task A")

    with pytest.raises(RuntimeError):
        manager.start("Task B")

def test_stop_completes_active_session():
    manager = SessionManager()

    session = manager.start("Stop completes active session")

    stopped = manager.stop()

    assert stopped is session
    assert not stopped.is_active
    assert manager.current_session() is None

def test_completed_sessions_are_retained():
    manager = SessionManager()

    session = manager.start("Start Session")
    manager.stop()

    completed = manager.completed_sessions()

    assert len(completed) == 1
    assert completed[0] is session

def test_cannot_stop_when_no_session_is_active():
    manager = SessionManager()

    with pytest.raises(RuntimeError):
        manager.stop()