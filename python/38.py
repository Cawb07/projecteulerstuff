'''
Created on Sep 6, 2013

https://projecteuler.net/problem=38

Take the number 192 and multiply it by each of 1, 2, and 3:

192 * 1 = 192
192 * 2 = 384
192 * 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 
192384576. We will call 192384576 the concatenated product of 
192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying 
by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which 
is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that 
can be formed as the concatenated product of an integer 
with (1,2, ... , n) where n > 1?

@author: Cawb07
'''
import time

def is_pandigital(i):
    n = str(i)
    
    if len(n) == 9:
        if "1" in n and "2" in n and "3" in n and "4" in n \
        and "5" in n and "6" in n and "7" in n and "8" in n \
        and "9" in n:
            return True
    else:
        return False
    

start = time.time()

pandigitals = []
for i in range(1, 10000):
    n = 9 / len(str(i))
    s = ""
    for j in range(1, n+1):
        if len(s) < 9:
            s += str(i*j)
    
    if is_pandigital(int(s)):
        pandigitals.append(int(s))

pandigitals.sort()
print pandigitals        

elapsed = time.time() - start
print "The elapsed time is %s seconds." % (elapsed)