from datetime import UTC, datetime
import pytest

from timewatcher_core.models import Session


def test_stop_sets_end_time():
    started_at = datetime(2026, 7, 12, 10, 0, tzinfo=UTC)
    ended_at = datetime(2026, 7, 12, 11, 30, tzinfo=UTC)

    session = Session(
        task="Write tests",
        start_time=started_at,
    )

    session.stop(ended_at)

    assert session.end_time == ended_at


def test_stop_raises_error_when_session_is_already_stopped():
    started_at = datetime(2026, 7, 12, 10, 0, tzinfo=UTC)
    ended_at = datetime(2026, 7, 12, 11, 30, tzinfo=UTC)

    session = Session(
        task="Write tests",
        start_time=started_at,
    )

    session.stop(ended_at)

    with pytest.raises(ValueError):
        session.stop()


# Is Active

def test_new_session_is_active():
    session = Session(
        task="Write code",
        start_time=datetime(2026, 7, 12, 10, 0, tzinfo=UTC),
    )

    assert session.is_active

def test_stopped_session_is_not_active():
    session = Session(
        task="Write code",
        start_time=datetime(2026, 7, 12, 10, 0, tzinfo=UTC),
    )

    session.stop(datetime(2026, 7, 12, 11, 0, tzinfo=UTC))

    assert not session.is_active


# Duration

from datetime import UTC, datetime, timedelta


def test_completed_session_returns_duration():
    started_at = datetime(2026, 7, 12, 10, 0, tzinfo=UTC)
    ended_at = datetime(2026, 7, 12, 11, 30, tzinfo=UTC)

    session = Session(
        task="Write documentation",
        start_time=started_at,
    )

    session.stop(ended_at)

    assert session.duration == timedelta(hours=1, minutes=30)

def test_active_session_has_no_duration():
    session = Session(
        task="Write documentation",
        start_time=datetime(2026, 7, 12, 10, 0, tzinfo=UTC),
    )

    assert session.duration is None

# Elapsed

def test_active_session_returns_elapsed_time():
    started_at = datetime(2026, 7, 14, 10, 0, tzinfo=UTC)

    session = Session(
        task="Write tests 7",
        start_time=started_at
    )

    assert session.elapsed is not None

# Session Start

def test_start_an_active_session():
    session = Session.start("Write Test 8")

    assert session.task == "Write Test 8"
    assert session.is_active
    assert session.end_time is None

# Domain Validation

def test_empty_task_name_raises_value_error():
    with pytest.raises(ValueError):
        Session.start("")

def test_end_time_cannot_be_before_start_time():
    started_at=datetime(2026, 7, 14, 11, 0, tzinfo=UTC)
    ended_at=datetime(2026, 7, 14, 10, 0, tzinfo=UTC)

    with pytest.raises(ValueError):
        Session(
             task="Write Test 9",
             start_time=started_at,
             end_time=ended_at
        )