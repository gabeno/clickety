#!/usr/bin/env python

import click


@click.command()
@click.argument("name", nargs=-1)
def cli(name):
    for n in name:
        print(f"Hello, {n}!")


if __name__ == "__main__":
    cli()
