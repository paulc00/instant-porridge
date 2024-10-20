"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Instant Porridge."""


if __name__ == "__main__":
    main(prog_name="instant-porridge")  # pragma: no cover
