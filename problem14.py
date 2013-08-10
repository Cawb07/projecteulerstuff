'''
Created on Aug 10, 2013

http://projecteuler.net/problem=14

@author: Cawb07
'''
import time

def collatz(i):
    Collatz = []
    Collatz.append(i)
    
    while i != 1:
        if i%2 == 0:
            i /= 2
            Collatz.append(i)
            
        else:
            i = (3*i) + 1
            Collatz.append(i)
    
    return Collatz
        

start = time.time()

largest = 0
length = 0
for i in range(1, 1000001):
    if len(collatz(i)) > length:
        length = len(collatz(i))
        largest = i

arr = collatz(largest)
print arr
print len(arr)

elapsed = (time.time() - start)
print "The elapsed time is %s seconds." % (elapsed)