# Write your code here
import re
def ababa(string):
     return re.fullmatch(r'(.+)(.+)\1\2\1', string)
 
 # dus \1 betekent dat je gaat 
 # kijken naar de eerste (.+) en 
 # wat dit ook is exact kopieert 
 # naar de plaats waar \1 staat