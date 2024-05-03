# Write your code here
def drop_ends(xs):
    value = len(xs) - 1
    xs = (xs[:value])
    return(drop_first(xs))


def drop_first(xs):
    return(xs[1:])