"""Approximate Pattern Matching Problem: Find all approximate occurrences of a pattern in a string.

Input: Strings Pattern and Text along with an integer d.
Output: All starting positions where Pattern appears as a substring of Text with at most d mismatches.
Code Challenge (3 points): Write a function ApproximatePatternMatching()
to solve the Approximate Pattern Matching Problem. (Make sure to use HammingDistance() as a subroutine!)"""


# Input:  Strings Pattern and Text along with an integer d
# Output: A list containing all starting positions where Pattern appears
# as a substring of Text with at most d mismatches
def ApproximatePatternMatching(Text, Pattern, d):
    positions = []  # initializing list of positions
    pl = len(Pattern)  # length of Pattern String
    tl = len(Text)  # length of Text string
    # both lengths used to get the amount of substrings in text that will be compared (tl-pl+1)
    hd = []  # list for HammingsDistances
    for i in range(tl - pl + 1):
        hd.append(HammingDistance(Text[i:i + pl], Pattern))
        # positions of substrings that fullfil the criteria of 3 or lower missmatches
    positions = [i for i, j in enumerate(hd) if j <= d]
    return positions


# Insert your Hamming distance function on the following line.
def HammingDistance(p, q):
    hd = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            hd += 1
    return hd
