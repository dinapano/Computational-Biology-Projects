"""Hamming Distance Problem:Compute the Hamming distance between two strings.

Input: Two strings of equal length.
Output: The Hamming distance between these strings."""

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

a="TGACCCGTTATGCTCGAGTTCGGTCAGAGCGTCATTGCGAGTAGTCGTTTGCTTTCTCAAACTCC"
b="GAGCGATTAAGCGTGACAGCCCCAGGGAACCCACAAAACGTGATCGCAGTCCATCCGATCATACA"

print(HammingDistance(a,b))