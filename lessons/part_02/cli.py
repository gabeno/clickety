#!/usr/bin/env python

import click


@click.option("--red", is_flag=True)
@click.command()
def cli(red):
    click.echo("Printing...", err=True)

    color = "red" if red else None
    click.secho("Hello!", fg=color)


if __name__ == "__main__":
    cli()
