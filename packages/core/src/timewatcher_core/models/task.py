from dataclasses import dataclass, field
from datetime import UTC, datetime
from uuid import UUID, uuid4 


@dataclass(slots=True)
class Task:
    """Represents a unit of work."""

    name: str
    id: UUID = field(default_factory=uuid4)
    description: str |None = None
    created_at: datetime = field(default_factory=lambda: datetime.now(UTC))

    def __post_init__(self) -> None:
        if not self.name.strip():
            raise ValueError("Task name cannot be empty")