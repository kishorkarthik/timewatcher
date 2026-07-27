import typer

import timewatcher_cli.bootstrap as bootstrap


def history() -> None:
    sessions = bootstrap.get_history.execute()

    if not sessions:
        typer.echo("No completed sessions.")
        return

    typer.echo("Completed Sessions")

    for session in sessions:
        typer.echo(session.task)