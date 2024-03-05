import math
# Write your code here
def median(ns):
    result = 0
    ns.sort()
    d = len(ns) / 2
    if len(ns) % 2 == 0:
        result = (ns[d] + ns[d - 1]) / 2
    else:
        result = ns[math.floor(len(ns) / 2)]
    return result

median([2,1,3,4])
        
