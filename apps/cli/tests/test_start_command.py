from typer.testing import CliRunner
from timewatcher_cli.app import app

import timewatcher_cli.bootstrap as bootstrap

runner = CliRunner()


def test_start_command_runs():
    result = runner.invoke(app, ["start", "Implement start CLI command"])

    assert result.exit_code == 0
    assert "Started: Implement start CLI command" in result.stdout
    assert bootstrap.manager.current_session() is not None