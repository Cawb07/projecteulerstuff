'''
[(1487, 4817, 8147), (2969, 6299, 9629)]
7.29567980766
'''
from utils import is_prime, primes

def permutations_of(length=1):
	def helper(n, permutations):
		digits = '0123456789'
		temp = []
		for permutation in permutations:
			for digit in digits:
				temp.append(permutation + digit)
		permutations = temp
		if len(permutations[0]) == n:
			return permutations
		else:
			return helper(n, permutations)
	return helper(length, ['1', '2', '3', '4', '5', '6', '7', '8', '9'])

def is_permutation(a, b):
	if set(a) == set(b):
		return True
	else:
		return False

def run():
	to_proc = []
	for prime in primes(1000,10000):
		to_proc.append(prime)
	to_proc.sort()
	permutations = []
	for i in to_proc[:]:
		if len(permutations) == 2:
			break
		for j in xrange(1, (10000-i)/2):
			second = str(i+j)
			if is_prime(i+j) and is_permutation(str(i), second):
				third = i+j+j
				if is_prime(third) and is_permutation(second, str(third)):
					permutations.append((i,i+j,i+j+j))
	print permutations


from timeit import Timer
t = Timer(lambda: run())
print t.timeit(number=1)
