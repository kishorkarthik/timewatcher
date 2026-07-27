from typer.testing import CliRunner

from timewatcher_cli.app import app

runner = CliRunner()


def test_stop_command_runs():
    runner.invoke(
        app,
        ["start", "Implement stop CLI command"],
    )

    result = runner.invoke(
        app,
        ["stop"],
    )

    assert result.exit_code == 0
    assert "Stopped: Implement stop CLI command" in result.stdout