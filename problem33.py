'''
Created on Sep 4, 2013

https://projecteuler.net/problem=33

The fraction 49/98 is a curious fraction, as an inexperienced 
mathematician in attempting to simplify it may incorrectly 
believe that 49/98 = 4/8, which is correct, is obtained by 
cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial 
examples.

There are exactly four non-trivial examples of this type of 
fraction, less than one in value, and containing two digits 
in the numerator and denominator.

If the product of these four fractions is given in its lowest 
common terms, find the value of the denominator.

@author: Cawb07
'''
import time
from fractions import Fraction

def curious(numer,denom):
    n = str(numer)
    d = str(denom)

    if len(n) == 2 and len(d) == 2:
        if n[1] == d[0]:
            if n != d:
                if d[1] != "0":
                    if Fraction(int(n[0]), int(d[1])) \
                    == \
                    Fraction(numer, denom):
                            return n + d


start = time.time()

nums = []
denoms = []
for i in range(10, 100):
    for j in range(10, 100):
        if type(curious(i, j)) == str:
            frac = (curious(i,j))
            nums.append(frac[0]+frac[1])
            denoms.append(frac[2]+frac[3])
            print frac

pro = 1
duct = 1

for i in range(0, len(nums)):
    pro *= int(nums[i])
    duct *= int(denoms[i])


print Fraction(pro, duct)

elapsed = time.time() - start
print "The elapsed time is %s seconds." % (elapsed)