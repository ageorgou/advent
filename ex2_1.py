import io

import pytest

def calculate_checksum(list_of_lines):
    """The checksum of a list of lines."""
    checksum = 0
    for line_of_numbers in list_of_lines:
        diff = max(line_of_numbers) - min(line_of_numbers)
        checksum += diff
    return checksum

def test_checksum():
    numbers = [[5, 1, 9, 5],
               [7, 5, 3],
               [2, 4, 6, 8]
    ]
    result = calculate_checksum(numbers)
    assert result == 18

if __name__ == "__main__":
    import sys
    infile = sys.argv[1]
    with open(infile) as text:
        text_as_numbers = ([int(word) for word in line.split()]
                           for line in text)
        result = calculate_checksum(text_as_numbers)
    print(result)
