'''
Created on Aug 16, 2013

https://projecteuler.net/problem=17

@author: Cawb07
'''
import time
import num2word_EN as num

def count_letters(s):
    count = 0
    for l in s:
        if l != " " and l != "-" and l != ",":
            count += 1
    
    return count


def letter_counts(n):
    count = 0
    for i in range(1, n+1):
        count += count_letters(num.to_card(i))
    
    return count



start = time.time()

print letter_counts(1000)

elapsed = time.time()-start
print "The elapsed time is %s seconds" % (elapsed)