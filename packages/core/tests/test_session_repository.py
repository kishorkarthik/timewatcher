from typing import Protocol

from timewatcher_core.repositories.session_repository import SessionRepository
from timewatcher_core.models import Session
from timewatcher_core.repositories.inmemory_session_repository import (
    InMemorySessionRepository,
)

def test_session_repository_is_a_protocol():
    assert issubclass(SessionRepository, Protocol)

def test_reposiotory_defines_save():
    assert hasattr(SessionRepository, "save")

def test_repository_starts_empty():
    repo = InMemorySessionRepository()

    assert repo.all() == []

def test_save_stores_session():
    repo = InMemorySessionRepository()

    session = Session.start("save the repo.")

    repo.save(session)

    assert repo.all() == [session]

def test_active_session_returns_running_session():
    repo = InMemorySessionRepository()

    session = Session.start("return running session.")
    repo.save(session)

    assert repo.active() is session

def test_completed_returns_completed_sessions():
    repo = InMemorySessionRepository()

    session = Session.start("return completed sessions")
    session.stop()

    repo.save(session)

    assert repo.completed() == [session]
    
