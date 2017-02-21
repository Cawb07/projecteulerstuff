

def is_prime(n):
	if n == 1: return False
	elif n == 2: return True
	elif n%2 == 0: return False
	
	# Elementary prime test borrowed from oeis.org/A000040.
	odds = 3
	while odds < n**.5+1:
		if n%odds == 0: return False
		odds += 2
	return True

def primes(i=2, end=None):
	if end:
		while i < end:
			if is_prime(i):
				yield i
			i += 1
	else:
		while True:
			if is_prime(i):
				yield i
			i += 1

def squares(i=1, end=None):
	if end:
		while i < end:
			yield i**2
			i += 1
	else:
		while True:
			yield i**2
			i += 1

def factor(n):
	def helper(i, factors):
		for prime in PRIMES:
			if prime > int(i/2):
				factors.add(i)
				return factors
			elif i%prime == 0:
				factors.add(prime)
				next = i/prime
				break
		return helper(next, factors)
	return helper(n, set())

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
