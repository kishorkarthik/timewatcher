import typer

from .commands.start import start
from .commands.stop import stop
from .commands.status import status

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

app.command()(stop)

app.command()(status)