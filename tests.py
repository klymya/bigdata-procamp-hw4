import sys
from io import StringIO
from contextlib import contextmanager

from mapper import mapper
from reducer import reducer


@contextmanager
def captured_output(inputs):
    new_out, new_in = StringIO(), StringIO(inputs)
    old_out, old_in = sys.stdout, sys.stdin
    try:
        sys.stdout, sys.stdin = new_out, new_in
        yield sys.stdout, sys.stdin
    finally:
        sys.stdout, sys.stdin = old_out, old_in


def test_mapper():
    with captured_output(
        "{}\n{}".format(
            ','.join(['test']*15), ','.join([str(i) for i in range(15)]))
    ) as (out, inn):
        mapper()

    output = out.getvalue().strip()
    assert output == '4\t11'


def test_reducer():
    with captured_output(
        "a\t1\nb\t3\nc\t5\na\t3"
    ) as (out, inn):
        reducer()

    output = out.getvalue().strip()
    assert output == 'c\t5.0\nb\t3.0\na\t2.0'


if __name__ == '__main__':
    test_mapper()
    test_reducer()
