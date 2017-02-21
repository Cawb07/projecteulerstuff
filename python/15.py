'''
Created on Aug 16, 2013

http://projecteuler.net/problem=15

The brute force method is commented out because it takes forever!!! Almost literally, in some cases.

@author: Cawb07
'''
import time
#import itertools
from math import factorial



'''
def find_paths(grid_side):
    i = 0
    turns = ""
    paths = []
    
    while i < grid_side:
        turns += "LR"
        i += 1

    perms = itertools.permutations(turns, grid_side*2)
    for p in perms:
        if p not in paths:
            paths.append(p)
    
    return paths



start = time.time()

paths = find_paths(5)
print paths
print len(paths)


elapsed = (time.time() - start)
print "The first time is %s" % (elapsed)


'''

def find_paths(grid_side):
    return n_choose_k(grid_side*2, grid_side)

def n_choose_k(n, k):
    return factorial(n)/(factorial(n-k)*factorial(k))


start2 = time.time()

print find_paths(20)

elapsed2 = (time.time() - start2)
print "The second time is %s" % (elapsed2)

