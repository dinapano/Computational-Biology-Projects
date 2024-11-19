""" The Hidden Message Problem is a well-defined computational problem==>NO"""


"""What is the most frequent 3-mer of "TAAACGTGAGAGAAACGTGCTGATTACACTTGTTCGTGTGGTAT" ?"""

def FrequencyMap(Text, k):
    freq = {}
    n = len(Text)
    for i in range(n-k+1):
        Pattern = Text[i:i+k]
        if Pattern in freq:
            freq[Pattern]+=1
        else:
            freq[Pattern] =1
    return freq

def FrequentWords(Text, k):
    words = []
    freq = FrequencyMap(Text, k)
    m = max(freq.values())
    for key in freq:
        """add each key to words whose corresponding frequency value is equal to m"""
        if freq[key] == m:
            words.append(key)
    return words

Text = "TAAACGTGAGAGAAACGTGCTGATTACACTTGTTCGTGTGGTAT"
k=3

print(FrequentWords(Text, k))