# Write your code here
def coins(one, two, five, goal):
    possible = False
    for x in range(0,one + 1):
        for y in range(0,two + 1):
            for z in range(0,five + 1):
                if x + y * 2 + z * 5 == goal:
                    possible = True
    return possible
    