from dataclasses import dataclass, field
from uuid import UUID, uuid4
from datetime import UTC, datetime

@dataclass(slots=True)
class Session:
    """Represents a single uninterrepted work session"""
    
    task: str
    start_time: datetime
    id: UUID = field(default_factory=uuid4)
    end_time: datetime | None = None

    def stop(self, ended_at: datetime | None = None) -> None:
        """Stops the session."""

        if self.end_time is not None:
            raise ValueError("Session has already been stopped.")
        
        self.end_time = ended_at or datetime.now(UTC)

    @property
    def is_active(self) -> bool:
        """Returns True if the session is currently running."""
        return self.end_time is None