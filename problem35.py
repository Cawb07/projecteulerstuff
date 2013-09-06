'''
Created on Sep 5, 2013

https://projecteuler.net/problem=35

The number, 197, is called a circular prime because all 
rotations of the digits: 197, 971, and 719, are themselves 
prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 
13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?

@author: Cawb07
'''
import time

def rotations(n):
    s = str(n)
    a = []
    rots = []
    
    for d in s:
        a.append(d)
    
    count = 0
    while count < len(a):
        rots.append(int(s))
        a.insert(0, a.pop())
        
        s = ""
        for d in a:
            s += d
        count += 1
    
    return rots


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


start = time.time()

rots = []
count = 0
for i in range(1, 1000000):
    if i%2 != 0:    
        rots = rotations(i)
        
        if all( (check_for_prime(rot) for rot in rots)):
            count += 1

print count

elapsed = time.time() - start
print "The elapsed time is %s seconds." % (elapsed)