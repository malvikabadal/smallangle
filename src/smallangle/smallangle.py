# make a list of numbers between 0 and 2pi and of the tan or the sin of these numbers

import click
import numpy as np
import pandas as pd
from numpy import pi

num = click.option(
    "-n",
    "--number",
    default=10,
    help="Amount of steps between 0 and 2pi.",
    show_default=True,
)


@click.group()
def cmd_group():
    pass


# make a subcommand sin
@cmd_group.command()
@num
def sin(number):
    """Make a list of numbers between 0 and 2pi and of the sin of these numbers.

    Args:
        number (int): amount of steps between 0 and 2pi
    """
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
    print(df)


# make a subcommand tan
@cmd_group.command()
@num
def tan(number):
    """Make a list of numbers between 0 and 2pi and of the tan of these numbers.

    Args:
        number (int): amount of steps between 0 and 2pi
    """
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
    print(df)


if __name__ == "__main__":
    cmd_group()
