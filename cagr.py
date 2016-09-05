from docopt import docopt


usage = """Usage: cagr.py [-h] --initial <initial> --final <final> [--years <years> | --months <months>]

-h --help    Show this
-i <initial>, --initial <initial>  Initial value
-f <final>, --final <final>        Final value
-y <years>, --years <years>        Years
-m <months>, --months <months>     Months
"""


def cagr(initial, final, years, months=None):
    """
    Compound Annual Growth Rate, given an initial and a final value for an investment,
    as well as the time elapsed (in years or fractions of years)
    """
    initial = float(initial)
    final = float(final)

    if years is not None:
        years = float(years)
    else:
        years = float(months) / 12.0

    if initial == 0:
        raise Exception('The initial value cannot be zero')

    if years == 0:
        raise Exception('The time period cannot be zero')

    return (final / initial) ** (1.0 / years) - 1


if __name__ == '__main__':
    args = docopt(usage, argv=None, help=True, version=None, options_first=False)
    print(cagr(args['--initial'], args['--final'], args['--years'], args['--months']))
