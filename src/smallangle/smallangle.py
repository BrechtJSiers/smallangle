import click
import numpy as np
from numpy import pi
import pandas as pd

@click.group()
def cmd_group():
    """Function to introduce different options to the smallangle commando.
    """
    pass  

@cmd_group.command()
@click.option(
    "-n",
    default=6
)

def sin(n):
    """ Gives the sin between 0 and 2pi.

    Args:
        n (integer): number of steps taken between 0 and 2pi.
    """
    x = np.linspace(0, 2 * pi, n)
    df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
    print(df)

@cmd_group.command()
@click.option(
    "-n",
    default=6
)
def tan(n):
    """Gives the tan between 0 and 2pi

    Args:
        n (integer): number of steps taken between 0 and 2pi.
    """
    x = np.linspace(0, 2 * pi, n)
    df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
    print(df)

if __name__ == "__main__":
    cmd_group()
