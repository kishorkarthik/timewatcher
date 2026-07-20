from typing import Protocol

from timewatcher_core.repositories.session_repository import SessionRepository

def test_session_repository_is_a_protocol():
    assert issubclass(SessionRepository, Protocol)

def test_reposiotory_defines_save():
    assert hasattr(SessionRepository, "save")
