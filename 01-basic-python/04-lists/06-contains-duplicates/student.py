# Write your code here
def contains_duplicates(xs):
    if not isinstance(xs, list):
        return False
    xs.sort()
    print(xs)
    previous = " "
    duplicates = False
    for item in xs:
        if item == previous:
            duplicates = True
        previous = item
    print(duplicates)
    return duplicates

