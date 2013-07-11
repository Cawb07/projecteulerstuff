'''
Created on Jul 1, 2013

A solution to problem 1 from projecteuler.net

projecteuler.net/problem=1

@author: Cawb07
'''

global y
y = 0

for x in range(1,1000):    
    if (x%3 == 0 or x%5 == 0):
        y = y + x
        print y