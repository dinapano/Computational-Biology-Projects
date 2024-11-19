"""Question 3
Compute PatternCount("AAA", "GACCATCAAAACTGATAAACTACTTAAAAATCAGT")."""

def PatternCount(Text, Pattern):
   count = 0
   for i in range(len(Text)-len(Pattern)+1):
       if Text[i:i+len(Pattern)] == Pattern:
           count = count+1
   return count

Text = "GACCATCAAAACTGATAAACTACTTAAAAATCAGT"
Pattern1="AAA"

print(PatternCount(Text, Pattern1))