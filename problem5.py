'''
Created on Jul 2, 2013

projecteuler.net/problem=5

@author: Cawb07
'''
import time

start = time.time()

z = 1000000000
x = 100000000

while (x < z):
    if(x%11 == 0 and x%12 == 0 and 
       x%13 == 0 and x%14 == 0 and x%15 == 0 and x%16 == 0 and
       x%17 == 0 and x%18 == 0 and x%19 == 0 and x%20 == 0):
        print x
    x = x + 1
    
elapsed = (time.time() - start)
print "result returned in %s seconds." % (elapsed)
