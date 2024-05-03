def is_prime(n):
    
    return (n >= 2 and all(n % x != 0 for x in range(2, n, 1)) )
    
print(is_prime(4))
    
def primes():
    
    