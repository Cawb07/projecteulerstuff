'''
Created on Aug 7, 2013

http://projecteuler.net/problem=11

@author: Cawb07
'''
import time
import numpy as np

def horizontals(g):
    products = []
    for i in range(0, 20):
        for j in range(0, 17):
            current = g[i][j]*g[i][j+1]*g[i][j+2]*g[i][j+3]
            if current != 0:
                products.append(current)
    
    return products

def verticals(g):
    products = []
    for j in range(0, 20):
        for i in range(0, 17):
            current = g[i][j]*g[i+1][j]*g[i+2][j]*g[i+3][j]
            if current != 0:
                products.append(current)
    
    return products

def forwardslashes(g):
    products = []
    for i in range(0, 17):
        for j in range(0, 17):
            current = g[i][j]*g[i+1][j+1]*g[i+2][j+2]*g[i+3][j+3]
            if current != 0:
                products.append(current)
    
    return products
    
def backslashes(g):
    products = []
    for i in range(0, 17):
        for j in range(0, 17):
            current = g[i+3][j]*g[i+2][j+1]*g[i+1][j+2]*g[i][j+3]
            if current != 0:
                products.append(current)
    
    return products
    

start = time.time()

grid = np.fromfile("20x20.txt", dtype=int, sep=" ").reshape(20,20)

products = []
for e in horizontals(grid):
    products.append(e)
    
for e in verticals(grid):
    products.append(e)
    
for e in backslashes(grid):
    products.append(e)
    
for e in forwardslashes(grid):
    products.append(e)

products.sort()
print products



elapsed = (time.time() - start)
print "The elapsed time is %s seconds." % (elapsed)