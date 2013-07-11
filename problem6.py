'''
Created on Jul 5, 2013

https://projecteuler.net/problem=6

@author: Cawb07
'''
import time

start = time.time()

sosquares = 0
squareos = 0
totalsum = 0

x = 0
y = 0

while (x < 100):
    x = x + 1
    sosquares = sosquares + x*x
    
while (y < 100):
    y = y + 1
    totalsum = totalsum + y   
    
squareos = totalsum * totalsum

difference = squareos - sosquares

print difference

elapsed = (time.time() - start)
print "found in %s seconds" % (elapsed)