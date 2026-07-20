from typing import Protocol

class SessionRepository(Protocol):
    """Contract for storing and retriving sessions."""

    def save(self, session: Session) -> None:
        """persist a session."""

    def active(self) -> Session | None:
        """Return the active session, if one exists."""
        
    def completed(self) -> list[Session]:
        """Return all completed session."""

    def all(self) -> list[Session]:
        """Return every stored session."""