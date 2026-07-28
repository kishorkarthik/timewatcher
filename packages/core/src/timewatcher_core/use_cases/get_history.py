from timewatcher_core.models import Session
from timewatcher_core.services.session_manager import SessionManager

class GetHistory:
    def __init__(self, manager: SessionManager) -> None:
        self._manger = manager

    def execute(self) -> list[Session]:
        return self._manger.completed_sessions()