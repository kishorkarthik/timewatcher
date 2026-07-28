from timewatcher_core.models import Session

class InMemorySessionRepository:
    def all(self) -> list[Session]:
        return list(self._sessions)

    def __init__(self) -> None:
        self._sessions: list[Session] = []

    def save(self, session: Session) -> None:
        for index, existing in enumerate(self._sessions):
          if existing.id == session.id:
            self._sessions[index] = session
            return

        self._sessions.append(session)

    def active_session(self) -> Session | None:
        for session in self._sessions:
            if session.is_active:
                return session

        return None

    def completed_sessions(self) -> list[Session]:
        return [
            session
            for session in self._sessions
            if not session.is_active
        ]