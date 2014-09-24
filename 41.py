'''
Created on Sep 11, 2013

https://projecteuler.net/problem=41

We shall say that an n-digit number is pandigital if it makes 
use of all the digits 1 to n exactly once. For example, 2143 
is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?

@author: Cawb07
'''
import time
from itertools import permutations

def pandigitals_len(n):
    if n > 9:
        print "Invalid length - too long."
        return False
    if n < 1:
        print "Invalid length - zero or negative number."
        return False
    
    pands = []
    
    s = ""
    for i in range(1, n+1):
        s += str(i)
        
    perms = permutations(s)
    index = 0
    for p in perms:
        pands.append("")
        for d in p:
            pands[index] += d
        index += 1
        
    return pands


def is_prime(n):
    if n == 1: return False
    elif n == 2: return True
    elif n%2 == 0: return False
    
    # Elementary prime test borrowed from oeis.org/A000040.
    odds = 3
    while odds < n**.5+1:
        if n%odds == 0: return False
        odds += 2
    return True


start = time.time()

pands = pandigitals_len(7)
for n in pands:
    if is_prime(int(n)):
        print n

elapsed = time.time() - start
print "The elapsed time is %s seconds." % (elapsed)