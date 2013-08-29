'''
Created on Aug 18, 2013

https://projecteuler.net/problem=22

Using names.txt (right click and 'Save Link/Target As...'), a 46K text file
containing over five-thousand first names, begin by sorting it into alphabetical
order. Then working out the alphabetical value for each name, multiply this value
by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is
worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would
obtain a score of 938 * 53 = 49714.

What is the total of all the name scores in the file?

@author: Cawb07
'''
import time
import string
import numpy as np

def sum_letters(s):
    sigma = 0
    
    for l in s:
        sigma += lettervalues[l]
    
    return sigma


start = time.time()

lettervalues = dict()
for i, letter in enumerate(string.ascii_uppercase):
    lettervalues[letter] = i + 1

names = np.loadtxt("names.txt", dtype=str, delimiter=",")
names.sort()
print names
print names[939]

total = 0
for i in range(0, len(names)):
    total += sum_letters(names[i])*(i+1)
    
print total

elapsed = time.time() - start
print "The elapsed time is %s seconds." % (elapsed)