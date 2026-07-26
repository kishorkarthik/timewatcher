from timewatcher_core.models import Session
from timewatcher_core.services.session_manager import SessionManager

class GetStatus:
    def __init__(self, manager: SessionManager) -> None:
        self._manager = manager

    def execute(self) -> Session | None:
        return self._manager.current_session()