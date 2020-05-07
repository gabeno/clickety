#!/usr/bin/env python

import click


@click.command()
@click.argument("name", nargs=-1)
@click.option("--greeting", "-g", default="Hello", help="The greeting to display")
@click.option("--question/--no-question", default=False, help="Make the greeting a question")
def cli(name, greeting, question):
    """Displays a greeting."""
    punctuation = "?" if question else "!"
    for n in name:
        print(f"{greeting}, {n}{punctuation}")


if __name__ == "__main__":
    cli()
