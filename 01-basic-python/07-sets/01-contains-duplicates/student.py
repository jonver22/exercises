# Write your code here
def contains_duplicates(xs):
    ls = set(xs)
    if len(xs) == len(ls):
        return False
    return True