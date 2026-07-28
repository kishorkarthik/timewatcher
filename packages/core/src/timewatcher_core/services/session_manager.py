from timewatcher_core.models import Session
from timewatcher_core.repositories.session_repository import SessionRepository


class SessionManager:
    def __init__(self, repository: SessionRepository) -> None:
        self._repository = repository
        self._active_session: Session | None = None

    def current_session(self) -> Session | None:
        if self._active_session is None:
            self._active_session = self._repository.active_session()

        return self._active_session

    def start(self, task: str) -> Session:
        if self.current_session() is not None:
            raise RuntimeError("An active session already exists.")

        session = Session.start(task)

        self._active_session = session
        self._repository.save(session)

        return session

    def stop(self) -> Session:
        session = self.current_session()

        if session is None:
            raise RuntimeError("No active session to stop.")

        session.stop()

        self._repository.save(session)

        self._active_session = None

        return session

    def completed_sessions(self) -> list[Session]:
        return self._repository.completed_sessions()