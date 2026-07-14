from dataclasses import dataclass, field
from uuid import UUID, uuid4
from datetime import UTC, datetime, timedelta

@dataclass(slots=True)
class Session:
    """Represents a single uninterrepted work session"""
    
    task: str
    start_time: datetime
    id: UUID = field(default_factory=uuid4)
    end_time: datetime | None = None

    def __post_init__(self) -> None:
        if not self.task.strip():
            raise ValueError("Task Name cannot be empty.")
        
        if self.end_time is not None and self.end_time < self.start_time:
            raise ValueError("End time cannot be before start time.")

    def stop(self, ended_at: datetime | None = None) -> None:
        """Stops the session."""

        if self.end_time is not None:
            raise ValueError("Session has already been stopped.")
        
        self.end_time = ended_at or datetime.now(UTC)

    @classmethod 
    def start(cls, task: str) -> "Session":
        return cls(
            task=task,
            start_time = datetime.now(UTC)
        )
    
    @property
    def is_active(self) -> bool:
        """Returns True if the session is currently running."""
        return self.end_time is None
    
    @property
    def duration(self) -> timedelta | None:
        """Returns the duration of a completed session."""

        if self.end_time is None:
            return None
        
        return self.end_time - self.start_time
    
    @property
    def elapsed(self) -> timedelta:
        """Returns the elapsed time of the session."""

        if self.end_time is None:
            return datetime.now(UTC) - self.start_time
        
        return self.end_time - self.start_time