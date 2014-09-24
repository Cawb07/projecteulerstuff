'''
Created on Sep 1, 2013

https://projecteuler.net/problem=27

Euler discovered the remarkable quadratic formula:

n^2 + n + 41

It turns out that the formula will produce 40 primes for the 
consecutive values n = 0 to 39. However, when n = 40, 
402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and 
certainly when n = 41, 41^2 + 41 + 41 is clearly divisible 
by 41.

The incredible formula  n^2 - 79n + 1601 was discovered, which 
produces 80 primes for the consecutive values n = 0 to 79. The 
product of the coefficients, -79 and 1601, is -126479.

Considering quadratics of the form:

n^2 + an + b, where |a| < 1000 and |b| < 1000

where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |-4| = 4
Find the product of the coefficients, a and b, for the 
quadratic expression that produces the maximum number of 
primes for consecutive values of n, starting with n = 0.

@author: Cawb07
'''
import time


def quadratic(n, a, b):
    return n**2 + a*n + b


def check_prime(n):
    if n == 1: return False
    elif n == 2: return True
    elif n%2 == 0: return False
    
    # Elementary prime test borrowed from oeis.org/A000040.
    odds = 3
    while odds < abs(n)**.5+1:
        if n%odds == 0: return False
        odds += 2
    return True


def formula1(n):
    return (n**2 + n + 41)


def formula2(n):
    return (n**2 - 79*n + 1601)


start = time.time()

coeff = {}

for i in range(-999, 1000):
    for j in range(-999, 1000):
        n = 0
        while check_prime(quadratic(n, i, j)) == True:
            n += 1
            coeff[str(i) + "," + str(j)] = n

longest = 0
k = ""
for key in coeff:
    if coeff[key] > longest:
        longest = coeff[key]
        k = key

print k + ": " + str(longest)
print -61*971

elapsed = time.time() - start
print "The elapsed time is %s seconds." % (elapsed)