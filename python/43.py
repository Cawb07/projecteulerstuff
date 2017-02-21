'''
Created on Sep 20, 2013

https://projecteuler.net/problem=43

The number, 1406357289, is a 0 to 9 pandigital number 
because it is made up of each of the digits 0 to 9 in 
some order, but it also has a rather interesting sub-
string divisibility property.

Let d_1 be the 1st digit, d_2 be the 2nd digit, and so on. 
In this way, we note the following:

* d_2d_3d_4=406 is divisible by 2
* d_3d_4d_5=063 is divisible by 3
* d_4d_5d_6=635 is divisible by 5
* d_5d_6d_7=357 is divisible by 7
* d_6d_7d_8=572 is divisible by 11
* d_7d_8d_9=728 is divisible by 13
* d_8d_9d_10=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this 
property.

@author: Cawb07
'''
import time
from itertools import permutations

def div_conditions(s):
    if int(s[1]+s[2]+s[3])%2 == 0:
        if int(s[2]+s[3]+s[4])%3 == 0:
            if int(s[3]+s[4]+s[5])%5 == 0:
                if int(s[4]+s[5]+s[6])%7 == 0:
                    if int(s[5]+s[6]+s[7])%11 == 0:
                        if int(s[6]+s[7]+s[8])%13 == 0:
                            if int(s[7]+s[8]+s[9])%17 == 0:
                                return True
    else:
        return False


def pandigitals_len(i, n):
    if n > 9:
        print "Invalid length - too long."
        return False
    elif n < 0:
        print "Invalid length - zero or negative number."
        return False
    
    pands = []
    
    s = ""
    for i in range(i, n+1):
        s += str(i)
        
    perms = permutations(s)
    index = 0
    for p in perms:
        pands.append("")
        for d in p:
            pands[index] += d
        index += 1
        
    return pands


start = time.time()

sigma = 0
pands = pandigitals_len(0,9)
for p in pands:
    if div_conditions(p):
        sigma += int(p)
print sigma

elapsed = time.time() - start
print "The elapsed time is %s seconds." % (elapsed)