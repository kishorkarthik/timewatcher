import typer

import timewatcher_cli.bootstrap as bootstrap


def stop() -> None:
    session = bootstrap.stop_session.execute()
    typer.echo(f"Stopped: {session.task}")