#!/usr/bin/env python

import click


@click.command()
@click.option("--red", is_flag=True)
def cli(red):
    print("Hello!")
    click.echo("Printing...", err=True)

    color = "red" if red else None
    click.secho("Hello!", fg=color)


if __name__ == "__main__":
    cli()
