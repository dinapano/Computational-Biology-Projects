"""Give all values of Skew for Genome equal to "GAGCCACCGCGATA" as a collection of space-separated integers.
Use the sample dataset below to help!

his array, denoted Skew, is defined by setting Skew[i] equal to the number of occurrences of G minus the number
of occurrences of C in the first i nucleotides of Genome (see figure below). We also set Skew[0] equal to zero.
Given a DNA string Genome, we can form its skew array by setting Skew[0] equal to 0, and then ranging﻿ through Genome.
At position i of Genome, if we encounter A or T, then we set Skew[i+1] equal to Skew[i]; if we encounter a G,
then we set Skew[i+1] equal to Skew[i]+1; if we encounter a C, then we set Skew[i+1] equal to Skew[i]-1."""


def calculate_skew(genome):
    # Initialization of the skew array with the first value set to 0
    skew = [0]

    # Iteration through each nucleotide in the genome
    for nucleotide in genome:
        if nucleotide == 'G':
            skew.append(skew[-1] + 1)  # Increment for G
        elif nucleotide == 'C':
            skew.append(skew[-1] - 1)  # Decrement for C
        else:
            skew.append(skew[-1])  # No change for A or T

    return skew

genome = "GAGCCACCGCGATA"
skew_values = calculate_skew(genome)

# Printing skew values as space-separated integers
print(" ".join(map(str, skew_values)))
