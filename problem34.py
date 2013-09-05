'''
Created on Sep 5, 2013

https://projecteuler.net/problem=34

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the 
factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included

@author: Cawb07
'''
import time
from math import factorial

def curious_factorial(n):
    s = str(n)
    sigma = 0
    
    for d in s:
        sigma += factorial(int(d))
    
    if sigma == n:
        return True
    else:
        return False


start = time.time()

cfacs = []
sigma = 0
for i in range(10, 100000):
    if curious_factorial(i):
        cfacs.append(i)
        sigma += i

print cfacs
print sigma

elapsed = time.time() - start
print "The elapsed time is %s seconds." % (elapsed)