"""To speed up SymbolArray(), we observe that when we slide a window one symbol to the right, the number of
occurrences of symbol in the window does not change much, and so regenerating the entire array from scratch is inefficient.

For example, in "CTGCTTCGCCCGCCGGACCGGCCTCGTGATGGGGTATGCTTCGCCCGCCGGA", the number of occurrences of C in the window
starting at position 1 ("TGCTTCGCCCGCCGGA") can be easily computed from the number of positions of occurrences of C in the
window starting at position 0 ("CTGCTTCGCCCGCCGG"). Indeed, we can view this sliding of the window as simply removing the
first symbol from the window (C) and adding a new symbol to the end (A). Thus, when shifting the window right by one symbol,
the number of occurrences of C in the window decreased by 1 and increased by 0. Once we compute that array[0] is equal to
8, we automatically know that array[1] is equal to 7."""

# Input:  Strings Genome and symbol
# Output: FasterSymbolArray(Genome, symbol)
def FasterSymbolArray(Genome, symbol):
    array = {}
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0:n//2]

    # look at the first half of Genome to compute first array value
    array[0] = PatternCount(symbol, Genome[0:n//2])

    for i in range(1, n):
        # start by setting the current array value equal to the previous array value
        array[i] = array[i-1]

        # the current array value can differ from the previous array value by at most 1
        if ExtendedGenome[i-1] == symbol:
            array[i] = array[i]-1
        if ExtendedGenome[i+(n//2)-1] == symbol:
            array[i] = array[i]+1
    return array

# Input:  Strings Text and Pattern
# Output: The number of times Pattern appears in Text
# HINT:   This code should be identical to when you last implemented PatternCount
def PatternCount(ExtendedGenome, Symbol):
    # type your code here
    count = 0
    for i in range(len(Symbol)-len(ExtendedGenome)+1):
        if Symbol[i:i+len(ExtendedGenome)] == ExtendedGenome:
            count = count+1
    return count

def SkewArray(Genome):
    # your code here
    skew = [0]

    # Iteration through each nucleotide in the genome
    for nucleotide in Genome:
        if nucleotide == 'G':
            skew.append(skew[-1] + 1)  # Increment for G
        elif nucleotide == 'C':
            skew.append(skew[-1] - 1)  # Decrement for C
        else:
            skew.append(skew[-1])  # No change for A or T

    return skew

# Input:  Two strings p and q
# Output: An integer value representing the Hamming Distance between p and q.
def HammingDistance(p, q):
    # your code here
    distance=0
    if len(p) != len(q):
        raise ValueError("Input strings must have the same length")

    # Iterate through the characters of both strings and compare them
    for i in range(len(p)):
        if p[i] != q[i]:
            distance += 1
    return distance

### DO NOT MODIFY THE CODE BELOW THIS LINE ###
import sys
lines = sys.stdin.read().splitlines()
print(FasterSymbolArray(lines[0],lines[1]))