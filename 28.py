'''
Created on Sep 1, 2013

https://projecteuler.net/problem=28

Starting with the number 1 and moving to the right in a 
clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the 
diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 
by 1001 spiral formed in the same way?

@author: Cawb07
'''
import time

# In this case all sizes will be some ODD integer.
def sum_diagonals(size):
    diag = 1
    sigma = 1
    
    for i in range(2, size, 2):
        count = 0
        while count < 4:
            diag += i
            sigma += diag
            count += 1
    
    return sigma


start = time.time()

print sum_diagonals(1001)

elapsed = time.time() - start
print "The elapsed time is %s seconds." % (elapsed)