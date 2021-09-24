#!/usr/bin/env python
"""reducer.py"""

import sys

TOP_N = 5


def reducer():
    delays = {}

    # input comes from STDIN
    for line in sys.stdin:
        # remove leading and trailing whitespace
        line = line.strip()

        # parse the input we got from mapper.py
        airline, delay = line.split('\t')

        # convert count (currently a string) to float
        try:
            delay = float(delay)
        except ValueError:
            # count was not a number, so silently
            # ignore/discard this line
            continue

        if airline in delays:
            delays[airline][0] += delay
            delays[airline][1] += 1
        else:
            delays[airline] = [delay, 1]

    delays = {k: v[0] / v[1] for k, v in delays.items()}
    sorted_delays = sorted(delays.items(), key=lambda kv: kv[1], reverse=True)

    for i in sorted_delays[:TOP_N]:
        print("{}\t{}".format(*i))


if __name__ == "__main__":
    reducer()
