"""What is the reverse complement of "TTGTGTC" ?"""

# Output: The reverse of Pattern
def Reverse(Pattern):
    # your code here
    return Pattern[::-1]

def Complement(Pattern):
    # your code here
    rev=""
    for i in Pattern:
        if i=="A":
            i=i.replace("A","T")
        elif i=="C":
            i=i.replace("C","G")
        elif i=="T":
            i=i.replace("T","A")
        elif i=="G":
            i=i.replace("G","C")
        rev+=i
    return rev

def ReverseComplement(Pattern):
    Pattern = Reverse(Pattern) # reverse all letters in a string
    Pattern = Complement(Pattern) # complement each letter in a string
    return Pattern

Pattern="TTGTGTC"
print(ReverseComplement(Pattern))