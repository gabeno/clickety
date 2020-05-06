#!/usr/bin/env python

import click


@click.command()
@click.argument("name", nargs=-1)
@click.option("--greeting", "-g", default="Hello")
@click.option("--question/--no-question", default=False)
def cli(name, greeting, question):
    punctuation = "?" if question else "!"
    for n in name:
        print(f"{greeting}, {n}{punctuation}")


if __name__ == "__main__":
    cli()
