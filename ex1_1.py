def matching_digits(seq):
    return [val for (i, val) in enumerate(seq) if seq[i-1] == val]

if __name__ == "__main__":
    import sys
    infile = sys.argv[1]
    with open(infile) as text:
        seq = [int(char) for char in text.read().strip()]
    print(sum(matching_digits(seq)))
