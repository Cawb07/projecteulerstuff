'''
Created on Sep 1, 2013

https://projecteuler.net/problem=27

Euler discovered the remarkable quadratic formula:

n^2 + n + 41

It turns out that the formula will produce 40 primes for the 
consecutive values n = 0 to 39. However, when n = 40, 
402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and 
certainly when n = 41, 41^2 + 41 + 41 is clearly divisible 
by 41.

The incredible formula  n^2 - 79n + 1601 was discovered, which 
produces 80 primes for the consecutive values n = 0 to 79. The 
product of the coefficients, -79 and 1601, is -126479.

Considering quadratics of the form:

n^2 + an + b, where |a| < 1000 and |b| < 1000

where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |-4| = 4
Find the product of the coefficients, a and b, for the 
quadratic expression that produces the maximum number of 
primes for consecutive values of n, starting with n = 0.

@author: Cawb07
'''
from math import pow

def T(s,p):
	pass

# a virus has probability p to be present in any individual
def to_opto(group_size, p):
	total_sheep = 25
	remainder_after_grouping = total_sheep % group_size
	p_negative_group = pow(1 - p, group_size)
	p_positive_group = 1 - p_negative_group
	expected_tests_per_group = 1 + (p_positive_group * group_size)
	if remainder_after_grouping == 0:
		average_test_total = expected_tests_per_group * (total_sheep / group_size)
	else:
		p_negative_final_group = pow(1 - p, remainder_after_grouping)
		p_positive_final_group = 1 - p_negative_final_group
		expected_tests_final_group = 1 + (p_positive_final_group * remainder_after_grouping)
		average_test_total = (expected_tests_per_group * 
			((total_sheep - remainder_after_grouping) / group_size))+expected_tests_final_group
	return average_test_total

results = []
for n in xrange(1,26):
	results.append(to_opto(n, .02))
results.sort()
print results