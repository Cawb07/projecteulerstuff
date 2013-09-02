'''
Created on Aug 30, 2013

https://projecteuler.net/problem=26

A unit fraction contains 1 in the numerator. The decimal 
representation of the unit fractions with denominators 2 
to 10 are given:

1/2    =     0.5
1/3    =     0.(3)
1/4    =     0.25
1/5    =     0.2
1/6    =     0.1(6)
1/7    =     0.(142857)
1/8    =     0.125
1/9    =     0.(1)
1/10    =     0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring 
cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest 
recurring cycle in its decimal fraction part.

@author: Cawb07
'''
import time
from decimal import *

getcontext().prec = 2000

start = time.time()

cycles = {}
for i in range(1, 1000):
    frac = Decimal(1)/i
    sfrac = str(frac)
    
    if len(sfrac) > 10:
        print "1/" + str(i) + " =", sfrac
        
        if i < 100 and i > 10:
            digits = sfrac[3:len(sfrac)]
            size = 1000
            one = ""
            two = ""
            
            while size > 5:
                one = digits[0:size]
                two = digits[size:size*2]
                
                if one == two:
                    cycles["1/" + str(i)] = one
                
                size -= 1
        
        if i < 1000 and i > 100:
            digits = sfrac[4:len(sfrac)]
            size = 1000
            one = ""
            two = ""
            
            while size > 5:
                one = digits[0:size]
                two = digits[size:size*2]
                
                if one == two:
                    cycles["1/" + str(i)] = one
                
                size -= 1

longest = ""
k = ""
for key in cycles:
    if len(cycles[key]) > len(longest):
        longest = cycles[key]
        k = key
print k + " = " + longest, "has the longest recurring cycle."
print len(longest)

elapsed = time.time() - start
print "The elapsed time is %s seconds." % (elapsed)