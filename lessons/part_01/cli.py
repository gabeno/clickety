#!/usr/bin/env python

import click


@click.command()
@click.argument("name", nargs=-1)
@click.option("--greeting", "-g", default="Hello", help="The greeting to display")
@click.option("--question/--no-question", default=False, help="Make the greeting a question")
@click.option("--int-option", type=int)
@click.option("--float-option", type=float)
@click.option("--bool-option", type=bool)
@click.option("--choice-option", type=click.Choice(["A", "B", "C"]))
def cli(name, greeting, question, int_option, float_option, bool_option, choice_option):
    """Displays a greeting."""
    punctuation = "?" if question else "!"
    for n in name:
        print(f"{greeting}, {n}{punctuation}")
    print(f"int: {int_option}")
    print(f"float: {float_option}")
    print(f"bool: {bool_option}")
    print(f"choice: {choice_option}")


if __name__ == "__main__":
    cli()
