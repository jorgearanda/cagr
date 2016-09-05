from docopt import docopt


usage = """Usage: cagr.py [-h] --initial <initial> --final <final> --years <years>

-h --help    Show this
-i <initial>, --initial <initial>  Initial value
-f <final>, --final <final>        Final value
-y <years>, --years <years>        Years
"""


def cagr(initial, final, years):
    """
    Compound Annual Growth Rate, given an initial and a final value for an investment,
    as well as the time elapsed (in years or fractions of years)
    """
    initial = float(initial)
    final = float(final)
    years = float(years)

    if initial == 0:
        raise Exception('The initial value cannot be zero')

    if years == 0:
        raise Exception('The number of years cannot be zero')

    return (final / initial) ** (1.0 / years) - 1


if __name__ == '__main__':
    args = docopt(usage, argv=None, help=True, version=None, options_first=False)
    cagr(args['--initial'], args['--final'], args['--years'])
