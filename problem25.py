'''
Created on Aug 30, 2013

https://projecteuler.net/problem=25

The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn-1 + Fn-2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the first term in the Fibonacci sequence to contain 1000 digits?

@author: Cawb07
'''
import time

def Fibonacci_digit(n):
    a = 0
    b = 1
    count = 1

    while True:
        count += 1
        
        c = a + b
        a = b
        b = c
        
        if  len(str(c)) == n:
            return c, "F" + str(count)

start = time.time()

print Fibonacci_digit(1000)

elapsed = time.time() - start
print "The elapsed time is %s seconds." % (elapsed)