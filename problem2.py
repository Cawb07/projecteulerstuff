'''
Created on Jul 1, 2013

projecteuler.net

@author: Cawb07
'''

global x
x = 1

global y
y = 0

global i
i = 0

while (x < 4000000 and y < 4000000):
    y = y + x
    x = x + y
    
    if (y < 4000000 and y%2 == 0):
        i = i + y
        print i
    if (x < 4000000 and x%2 == 0):
        i = i + x
        print i