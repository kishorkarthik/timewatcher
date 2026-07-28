from typer.testing import CliRunner

from timewatcher_cli.app import app

runner = CliRunner()


def test_history_returns_completed_sessions():
    runner.invoke(
        app,
        ["start", "Implement history CLI command"],
    )

    runner.invoke(
        app,
        ["stop"],
    )

    result = runner.invoke(
        app,
        ["history"],
    )

    assert result.exit_code == 0
    assert "Completed Sessions" in result.stdout
    assert "Implement history CLI command" in result.stdout

def test_history_returns_no_completed_sessions():
    result = runner.invoke(
        app,
        ["history"],
    )

    assert result.exit_code == 0
    assert "No completed sessions." in result.stdout