from timewatcher_core.models import Session

class SessionManager:
    def __init__(self) -> None:
        self._active_session: Session | None = None
        self._completed_sessions: list[Session] = []

    def current_session(self) -> Session | None:
        return self._active_session
    
    def start(self, task: str) -> Session:
        if self._active_session is not None:
            raise RuntimeError("An active session already exists")
        
        session = Session.start(task)
        self._active_session = session
        return session
    
    def stop(self) -> Session:
        if self._active_session is None:
            raise RuntimeError("No active session to stop.")
        
        session = self._active_session
        session.stop()

        self._completed_sessions.append(session)
        self._active_session = None

        return session
    
    def completed_sessions(self) -> list[Session]:
        return list(self._completed_sessions)