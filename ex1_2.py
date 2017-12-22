def matching_digits(seq):
    # len(seq) guaranteed to have an even length
    offset = len(seq) // 2
    return [val for (i, val) in enumerate(seq) if seq[i-offset] == val]

if __name__ == "__main__":
    import sys
    infile = sys.argv[1]
    with open(infile) as text:
        seq = [int(char) for char in text.read().strip()]
    print(sum(matching_digits(seq)))
