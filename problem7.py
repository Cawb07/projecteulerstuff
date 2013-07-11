'''
Created on Jul 7, 2013

https://projecteuler.net/problem=7

@author: Cawb07
'''
import time

def check_for_prime(n):
    if n%2 == 0: return False
    
    # Elementary prime test borrowed from oeis.org/A000040.
    # + 1 is used because for ints, .7 = 0 in Python.
    odds = 3
    while odds < n**.5+1:
        if n%odds == 0: return False
        odds += 2
    return True

def nth_prime(n):
    first_prime = 2
    count = 1
    iter = 3
    while count < n:
        if check_for_prime(iter):
            prime = iter
            count += 1
        iter += 2
    return prime

start = time.time()
prime = nth_prime(10001)
elapsed = (time.time() - start)

print "The 10001th prime is %s. It was found in %s seconds." % (prime, elapsed)