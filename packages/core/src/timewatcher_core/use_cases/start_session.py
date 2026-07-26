from timewatcher_core.services.session_manager import SessionManager
from timewatcher_core.models import Session

class StartSession:
    def __init__(self, manager: SessionManager) -> None:
        self._manager = manager

    def execute(self, task:str) -> Session:
        return self._manager.start(task)



    