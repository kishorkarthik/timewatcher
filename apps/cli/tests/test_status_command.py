from typer.testing import CliRunner

from timewatcher_cli.app import app

runner = CliRunner()


def test_status_returns_active_session():
    runner.invoke(
        app,
        ["start", "Implement status CLI command"],
    )

    result = runner.invoke(
        app,
        ["status"],
    )

    assert result.exit_code == 0
    assert "Active: Implement status CLI command" in result.stdout

def test_status_returns_no_active_session():
    result = runner.invoke(
        app,
        ["status"],
    )

    assert result.exit_code == 0
    assert "No active session." in result.stdout