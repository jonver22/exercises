# Write your code here
def remove_duplicates(xs):
    duplicate = set()
    result = []
    for item in xs:
        if item not in found:
            result.append(item)
            found.add(item)
    return result

print(remove_duplicates([1,2,2,3,2]))