"""Write a function MinimumSkew() taking as input a DNA string Genome and returning all integers i minimizing Skew[i]
for Genome. Then add this function to Replication.py.

Hint: make sure to call Skew(Genome) as a subroutine, and keep in mind that Python has a built-in min() function in
addition to max()."""


# Input:  A DNA string Genome
# Output: A list containing all integers i minimizing Skew(Prefix_i(Text)) over all values of i (from 0 to |Genome|)
def MinimumSkew(Genome):
    positions = []  # output variable
    # your code here
    skew_raw = SkewArray(Genome)  # set a variable equal to SkewArray(Genome)
    # find the minimum value of all values in the skew array
    values_min = min(skew_raw.values())
    # range over the length of the skew array and add all positions achieving the min to positions
    for key, value in skew_raw.items():
        if value == values_min:
            positions.append(key)
    return positions


# Input:  A String Genome
# Output: SkewArray(Genome)
# HINT:   This code should be taken from the last Code Challenge.
def SkewArray(Genome):
    skew = {}  # output variable
    # your code here
    # Iteration through each nucleotide in the genome
    current_skew = 0
    for index, nucleotide in enumerate(Genome):
        if nucleotide == "G":
            current_skew += 1
        elif nucleotide == "C":
            current_skew -= 1

        skew[index + 1] = current_skew

    return skew