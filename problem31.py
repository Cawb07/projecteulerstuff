'''
Created on Sep 2, 2013

https://projectpoundler.net/problems

In England the currency is made up of pound, pound, and pence, 
p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, 1 pound (100p) and 2 pound (200p).

It is possible to make pound2 in the following way:

1*1 pound + 1*50p + 2*20p + 1*5p + 1*2p + 3*1p
How many different ways can 2 pound be made using any number of 
coins?

@author: Cawb07
'''
import time

values = [1, 2, 5, 10, 20, 50, 100, 200]
ways = [1] + [0]*200


start = time.time()

for v in values:
    for i in range(v, 201):
        ways[i] += ways[i-v]

print ways[200]

elapsed = time.time() - start
print "The elapsed time is %s seconds." % (elapsed)