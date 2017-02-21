'''
Preparing complete
Mulitprocessing complete
134043
253.266087055
'''
from multiprocessing import Pool

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

def primes_desc(i=1):
	while i != 1:
		if is_prime(i):
			yield i
		i -= 1

PRIMES = []
for prime in primes_desc(1000000):
	PRIMES.append(prime)
PRIMES.sort()

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

def prime_factors(i):
	factors = factor(i)
	if factors and len(factors) == 4:
		return i
	else:
		return None

def run():
	to_proc = []
	i = 1
	while i < 1000000:
		i += 1
		if is_prime(i):
			continue
		else:
			to_proc.append(i)
	print 'Preparing complete'
	pool = Pool(4)
	results = pool.map(prime_factors, to_proc)
	pool.close()
	pool.join()
	print "Mulitprocessing complete"
	uniqued = set(results)
	uniqued.remove(None)
	uniqued = list(uniqued)
	uniqued.sort()
	for n in xrange(len(uniqued)):
		try:
			goal = (4*uniqued[n]) +  6
			actual = uniqued[n] + uniqued[n+1] + uniqued[n+2] + uniqued[n+3]
			if goal == actual:
				print uniqued[n]
				break
		except IndexError:
			break

	# for n in xrange(len(uniqued)):
	# 	try:
	# 		goal = (3*uniqued[n]) +  3
	# 		actual = uniqued[n] + uniqued[n+1] + uniqued[n+2]
	# 		if goal == actual:
	# 			print uniqued[n]
	# 			break
	# 	except IndexError:
	# 		break


from timeit import Timer
t = Timer(lambda: run())
print t.timeit(number=1)
