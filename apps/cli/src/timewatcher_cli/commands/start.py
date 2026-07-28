import typer

import timewatcher_cli.bootstrap as bootstrap


def start(task: str) -> None:
    session = bootstrap.start_session.execute(task)
    typer.echo(f"Started: {session.task}")