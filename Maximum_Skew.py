""" Identify the value of i for which the skew array of "CATTCCAGTACTTCGATGATGGCGTGAAGA" attains a maximum value.

Report the position of the first occurrence only, with 1-based numeration (i.e. Skew[1] corresponds to "C" here)"""

def find_max_skew_position(genome):
    skew = [0]  # Initialize the skew array with the first value as 0
    max_skew = 0
    position = 0

    for i, nucleotide in enumerate(genome):
        if nucleotide == 'G':
            skew.append(skew[-1] + 1)
        elif nucleotide == 'C':
            skew.append(skew[-1] - 1)
        else:
            skew.append(skew[-1])

        # Update max_skew and position if the current skew is greater
        if skew[i + 1] > max_skew:
            max_skew = skew[i + 1]
            position = i + 1  # Store the 1-based index

    return position


# Example usage
genome = "CATTCCAGTACTTCGATGATGGCGTGAAGA"
max_skew_position = find_max_skew_position(genome)

print(f"The position of the first occurrence of the maximum skew value is: {max_skew_position}")
