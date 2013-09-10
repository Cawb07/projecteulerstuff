'''
Created on Sep 6, 2013

https://projecteuler.net/problem=36

The decimal number, 585 = 10010010012 (binary), is palindromic 
in both bases.

Find the sum of all numbers, less than one million, which are 
palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may 
not include leading zeros.)

@author: Cawb07
'''
import time

def is_palindrome(s):
    backwards = ""
    
    for i in range(len(s)-1, -1, -1):
        backwards += s[i]
    
    if backwards == s:
        return True
    else:
        return False


def trim_bin(n):
    s = bin(n)[2:]
    return s


def sum(d):
    sigma = 0
    
    for e in d:
        sigma += e
    
    return sigma
    

start = time.time()


DBpalindromes = []
for i in range(1, 1000000):
    if is_palindrome(str(i)) and is_palindrome(trim_bin(i)):
        DBpalindromes.append(i)
        
print sum(DBpalindromes)

elapsed = time.time() - start
print "The elapsed time is %s seconds." % (elapsed)