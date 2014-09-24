'''
Created on Aug 7, 2013

http://projecteuler.net/problem=9

@author: Cawb07
'''
import math as m

def check_triplet(a,b):
    if m.sqrt(a**2 + b**2)%1 == 0:
        return True
    else:
        return False

triplets = []

for i in range(1, 999):
    for j in range(1, 999):
        if j<i and j != i:
            if check_triplet(j,i):
                triplets.append([j, i, m.sqrt(j**2 + i**2)])
                
print triplets

for t in triplets:
    sigma = 0
    for i in t:
        sigma += i
    
    if sigma == 1000:
        print t

print 200*375*425