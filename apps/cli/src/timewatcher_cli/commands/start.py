import typer

from timewatcher_cli.bootstrap import start_session


def start(task: str) -> None:
    session = start_session.execute(task)
    typer.echo(f"Started: {session.task}")