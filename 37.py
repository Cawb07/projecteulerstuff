'''
Created on Sep 6, 2013

https://projecteuler.net/problem=37

The number 3797 has an interesting property. Being prime 
itself, it is possible to continuously remove digits from 
left to right, and remain prime at each stage: 3797, 797, 97, 
and 7. Similarly we can work from right to left: 3797, 379, 
37, and 3.

Find the sum of the only eleven primes that are both 
truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable 
primes.

@author: Cawb07
'''
import time

def sum(d):
    sigma = 0
    
    for e in d:
        sigma += e
    
    return sigma


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


def truncleft_prime(n):
    if n==2 or n==3 or n==5 or n==7:
        return False
    
    i = n
    s = str(n)
    allprime = True
    
    while allprime:    
        allprime = check_for_prime(i)
        i -= int(s[0])*10**(len(s)-1)
        s = str(i)
        
        if s == "0":
            break    
    
    return allprime
    

def truncright_prime(n):
    if n==2 or n==3 or n==5 or n==7:
        return False
    
    i = n
    allprime = True
    
    while allprime:
        allprime = check_for_prime(i)
        i -= i%10
        i /= 10
        
        if i == 0:
            break
    
    return allprime


start = time.time()

truncprimes = []
for i in range(1, 1000000):
    if truncleft_prime(i) and truncright_prime(i):
        truncprimes.append(i)

print truncprimes
print len(truncprimes)
print sum(truncprimes)

elapsed = time.time() - start
print "The elapsed time is %s seconds." % (elapsed)