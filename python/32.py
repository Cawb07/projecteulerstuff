'''
Created on Sep 3, 2013

https://projecteuler.net/problem=32

We shall say that an n-digit number is pandigital if it makes 
use of all the digits 1 to n exactly once; for example, the 
5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 * 186 = 7254, 
containing multiplicand, multiplier, and product is 1 through 
9 pandigital.

Find the sum of all products whose multiplicand/multiplier/
product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so 
be sure to only include it once in your sum.

@author: Cawb07
'''
import time

def is_pandigital(a,b,p):
    n = str(a)+str(b)+str(p)
    
    if len(n) == 9:
        if "1" in n and "2" in n and "3" in n and "4" in n and "5" in n and "6" in n and "7" in n and "8" in n and "9" in n:
            return True
    else:
        return False


def sum(d):
    sigma = 0
    
    for e in d:
        sigma += e
    
    return sigma


start = time.time()

products = []
for i in range(101, 9999):
    for j in range(1, 100):
        if is_pandigital(i,j, i*j):
            if i*j not in products:
                products.append(i*j)

print sum(products)
        
elapsed = time.time() - start
print "The elapsed time is %s seconds." % (elapsed)