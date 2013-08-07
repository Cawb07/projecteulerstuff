'''
Created on Aug 7, 2013

http://projecteuler.net/problem=10

@author: Cawb07
'''
import time

def check_for_prime(n):
    if n == 1: return False
    elif n == 2: return True
    elif n%2 == 0: return False
    
    # Elementary prime test borrowed from oeis.org/A000040.
    odds = 3
    while odds < n**.5+1:
        if n%odds == 0: return False
        odds += 2
    return True

def sum_primes(n):
    sigma = 0
    
    for i in range(1, n+1):
        if check_for_prime(i):
            sigma += i
    
    return sigma


start = time.time()

print sum_primes(2000000)

elapsed = (time.time() - start)
print "The elapsed time is %s seconds." % (elapsed)