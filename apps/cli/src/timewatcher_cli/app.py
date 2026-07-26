import typer

from .commands.start import start

app = typer.Typer(
    name="timewatcher",
    help="Keep your hands on the keyboard—log your active work hours via the CLI.",
    no_args_is_help=True,
)

@app.callback()
def main() -> None:
    """TimeWatcher CLI."""
    pass

app.command()(start)