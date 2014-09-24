'''
Created on Aug 18, 2013

https://projecteuler.net/problem=20

For example, 10! = 10 * 9 * 8 ... * 3 * 2 * 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!

@author: Cawb07
'''
import time

def factorial(n):
    product = 1
    
    for i in range(1, n+1):
        product *= i
    
    return product

def int_to_array(n):
    array = []
    int = n
    
    while int != 0:
        d = int%10
        array.append(d)
        int = (int-d)/10
        
    
    return array

def sum(d):
    sigma = 0
    
    for e in d:
        sigma += e
    
    return sigma

start = time.time()

digits = int_to_array(factorial(100))
print sum(digits)

elapsed = time.time() - start
print "The elapsed time is %s seconds." % (elapsed)