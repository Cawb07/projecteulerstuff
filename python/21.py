'''
Created on Aug 18, 2013

https://projecteuler.net/problem=21

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

@author: Cawb07
'''
import time

def proper_divisors(n):
    divisors = []
    i = 1
    
    if (n/2)%1 == 0:
        while i < (n/2)+1:
            if n%i == 0:
                divisors.append(i)
            i += 1
    else:
        while i < (n+1)/2:
            if n%i == 0:
                divisors.append(i)
            i += 1
    
    return divisors


def sum(d):
    sigma = 0
    
    for e in d:
        sigma += e
    
    return sigma


def amicables_under(n):
    amicables = []
    
    for i in range(1, n):
        pair = sum(proper_divisors(i))
        
        if pair != i:    
            if sum(proper_divisors(pair)) == i:
                amicables.append(i)
    
    return amicables


start = time.time()

print sum(amicables_under(10000))

elapsed = time.time() - start
print "The elapsed time is %s seconds." % (elapsed)