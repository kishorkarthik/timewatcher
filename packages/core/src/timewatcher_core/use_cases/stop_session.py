from timewatcher_core.models import Session
from timewatcher_core.services.session_manager import SessionManager

class StopSession:
    def __init__(self, manager: SessionManager) -> None:
        self._manager = manager

    def execute(self) -> Session:
        return self._manager.stop()