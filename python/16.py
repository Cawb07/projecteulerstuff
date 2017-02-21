'''
Created on Aug 16, 2013

https://projecteuler.net/problem=16

@author: Cawb07
'''
import time

def sum_digits(n):
    s = str(n)
    sigma = 0
    
    for i in s:
        sigma += int(i)
    
    return sigma



start = time.time()

print sum_digits(2**1000)

elapsed = (time.time() - start)
print "The elapsed time is %s seconds." % (elapsed)