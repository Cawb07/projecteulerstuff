'''
Created on Sep 12, 2013

https://projecteuler.net/problem=42

The nth term of the sequence of triangle numbers is given by, 
t_n = (1/2)n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding 
to its alphabetical position and adding these values we form 
a word value. For example, the word value for SKY is 19 + 11 
+ 25 = 55 = t_10. If the word value is a triangle number then 
we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), 
a 16K text file containing nearly two-thousand common English 
words, how many are triangle words?

@author: Cawb07
'''
import time
import string
import numpy as np

def is_trinum(n, bound):
    for i in range(1, bound+1):
        if (i*(i+1))/2 == n:
            return True


def sum_letters(s):
    sigma = 0
    
    lettervalues = dict()
    for i, letter in enumerate(string.ascii_uppercase):
        lettervalues[letter] = i + 1
    
    for l in s:
        sigma += lettervalues[l]
    
    return sigma


start = time.time()

words = np.loadtxt("words.txt", dtype=str, delimiter=",")

count = 0
for w in words:
    if is_trinum(sum_letters(w), 100):
        count += 1
print count

elapsed = time.time() - start
print "The elapsed time is %s seconds." % (elapsed)