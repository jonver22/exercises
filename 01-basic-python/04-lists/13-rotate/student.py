# Write your code here
def rotate(xs, n):
    while n > 0:
        n -= 1 
        j = xs[0]
        del xs[0]
        xs.append(j)
    return xs