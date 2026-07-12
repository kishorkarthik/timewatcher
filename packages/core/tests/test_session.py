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