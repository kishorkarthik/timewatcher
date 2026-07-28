from typer.testing import CliRunner

from timewatcher_cli.app import app


runner = CliRunner()


def test_complete_cli_workflow():
    start_result = runner.invoke(
        app,
        ["start", "Complete workflow test"],
    )

    assert start_result.exit_code == 0
    assert "Started: Complete workflow test" in start_result.stdout

    status_result = runner.invoke(
        app,
        ["status"],
    )

    assert status_result.exit_code == 0
    assert "Active: Complete workflow test" in status_result.stdout

    stop_result = runner.invoke(
        app,
        ["stop"],
    )

    assert stop_result.exit_code == 0
    assert "Stopped: Complete workflow test" in stop_result.stdout

    history_result = runner.invoke(
        app,
        ["history"],
    )

    assert history_result.exit_code == 0
    assert "Complete workflow test" in history_result.stdout