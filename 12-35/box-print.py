#! /usr/bin/env python3

"""

***************
*             *
*             *
*             *
***************

"""

import sys

# Stop program if user enters fewer than 3 arguments:
if len(sys.argv) < 4:
    raise Exception('Use the following syntax: ./box-print.py "*" 15 5')


def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('"symbol" must be a string of length 1.')
    if (int(width) < 2) or (int(height) < 2):
        raise Exception('"width" and "height" must be 2 or greater."')

    print(symbol * int(width))

    for i in range(int(height) - 2):
        print(symbol + (' ' * (int(width) - 2)) + symbol)

    print(symbol * int(width))


boxPrint(sys.argv[1], sys.argv[2], sys.argv[3])
