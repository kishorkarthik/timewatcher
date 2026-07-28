import pytest

from timewatcher_core.models import Task

# has_expected_defaults
def test_new_task_has_expecte_defaults():
    task = Task(name="Task Test 1")

    assert task.name == "Task Test 1"
    assert task.description is None
    assert task.id is not None
    assert task.created_at is not None

# Task Validation
def test_empty_task_name_rises_error():
    with pytest.raises(ValueError):
        Task(name="")