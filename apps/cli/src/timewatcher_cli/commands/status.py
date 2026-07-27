import typer

import timewatcher_cli.bootstrap as bootstrap


def status() -> None:
    session = bootstrap.get_status.execute()

    if session is None:
        typer.echo("No active session.")
        return

    typer.echo(f"Active: {session.task}")