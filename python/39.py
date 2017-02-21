'''
Created on Sep 6, 2013

https://projecteuler.net/problem=39

If p is the perimeter of a right angle triangle with integral 
length sides, {a,b,c}, there are exactly three solutions 
for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p <= 1000, is the number of solutions 
maximised?

@author: Cawb07
'''
import time

def right_triangles(p):
    count = 0
    
    if p < 1000:
        for a in range(1, p/2):
            for b in range(a, p):
                c = p-a-b
                if a**2 + b**2 == c**2:
                    count += 1
                    
    return count


start = time.time()

perimeters = []
longest = 0
for p in range(1, 1001):
    if right_triangles(p) != 0:
        if right_triangles(p) > longest:
            longest = right_triangles(p)
            print str(p) + " with " + \
            str(right_triangles(p)) + " triangles."


elapsed = time.time() - start
print "The elapsed time is %s seconds." % (elapsed)