from typer.testing import CliRunner

from timewatcher_cli.app import app
from timewatcher_cli.bootstrap import manager

runner = CliRunner()


def test_start_command_runs():
    result = runner.invoke(app, ["start", "Implement start CLI command"])

    assert result.exit_code == 0
    assert "Started: Implement start CLI command" in result.stdout
    assert manager.current_session() is not None