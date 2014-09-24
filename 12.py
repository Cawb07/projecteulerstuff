'''
Created on Aug 7, 2013

http://projecteuler.net/problem=12

@author: Cawb07
'''
import time
import operator

def get_trinumber(n):
    sigma = 0
    for i in range(1, n+1):
        sigma += i
        
    return sigma

# A slightly efficient superset of primes.
def primes_plus():
    yield 2
    yield 3
    i = 5
    while True:
        yield i
        if i % 6 == 1:
            i += 2
        i += 2
        
# Returns a dict d with n = product p ^ d[p]
def get_prime_decomp(n):
    d = {}
    primes = primes_plus()
    for p in primes:
            while n % p == 0:
                n /= p
                d[p] = d.setdefault(p, 0) + 1
            if n == 1:
                return d

def count_divisors(n):
    d = get_prime_decomp(n)
    powers_plus = map(lambda x: x+1, d.values())
    return reduce(operator.mul, powers_plus, 1)

def trinumber_with_divisors(n):
    index = 1
    
    while count_divisors(get_trinumber(index)) <= n:
        index += 1
    
    return get_trinumber(index)

start = time.time()

print trinumber_with_divisors(500)

elapsed = (time.time() - start)
print "The elapsed time is %s seconds." % (elapsed)