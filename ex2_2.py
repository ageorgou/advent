import io

import pytest

def calculate_sum(list_of_lines):
    return sum(div(line) for line in list_of_lines)


def is_int(num):
    """Check whether a number is integer-valued."""
    return int(num) == num


def div(seq):
    """Return the ratio of the evenly divisible numbers from a list.

    The list is guaranteed to contain exactly two evenly divisible numbers.
    """
    for (i, n) in enumerate(seq):
        # try dividing this number with all others
        # (in fact, we can only consider the subsequent numbers,
        # and check the ratio both ways)
        for j in range(i+1, len(seq)):
            ratio1 = seq[j] / seq[i]
            ratio2 = seq[i] / seq[j]
            for result in [ratio1, ratio2]:
                # is the result an integer? if so, done
                if is_int(result):
                    return int(result)


def test_is_int():
    inputs = [3.2, -3.2, 5.0, -5.0, 4, -1, 0]
    outputs = [False, False, True, True, True, True, True]
    for (inp, outp) in zip(inputs, outputs):
        assert is_int(inp) == outp


def test_div():
    assert div([10, 4, 3, 5]) == 2
    assert div([5, 3, 10, 4]) == 2


def test_whole():
    numbers = [[5, 9, 2, 8],
               [9, 4, 7, 3],
               [3, 8, 6, 5]
    ]
    result = calculate_sum(numbers)
    assert result == 9


if __name__ == "__main__":
    import sys
    infile = sys.argv[1]
    with open(infile) as text:
        # Conver the text to an iterable of numbers
        text_as_numbers = ([int(word) for word in line.split()]
                           for line in text)
        result = calculate_sum(text_as_numbers)
    print(result)
