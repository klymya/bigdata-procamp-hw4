#!/usr/bin/env python
"""mapper.py"""

import sys

AIRLINE_IDX = 4
DEPARTURE_DELAY_IDX = 11


def mapper():
    # input comes from STDIN (standard input)
    for line in sys.stdin:
        # remove leading and trailing whitespace
        line = line.strip()
        # split the line into values
        values = line.split(',')

        try:
            float(values[DEPARTURE_DELAY_IDX])
        except ValueError:
            continue

        print('{}\t{}'.format(values[AIRLINE_IDX], values[DEPARTURE_DELAY_IDX]))


if __name__ == "__main__":
    mapper()
