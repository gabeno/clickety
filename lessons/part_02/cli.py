#!/usr/bin/env python

import click


@click.command()
@click.argument("infile", type=click.File("r"), default="-")
@click.argument("outfile", type=click.File("w"), default="-")
def cli(infile, outfile):
    text = infile.read()
    click.echo(text, file=outfile, nl=False)
    click.echo(f"Input length: {len(text)}", err=True)


if __name__ == "__main__":
    cli()
