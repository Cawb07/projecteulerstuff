'''
Exception: The smallest odd composite that cannot we written as the sum of a prime and twice a squre is 5777
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

def primes(i=1):
	while True:
		if is_prime(i):
			yield i
		i += 1

def squares(i=1):
	while True:
		yield i**2
		i += 1

# for square in squares():
# 	print square
# 	if square == 10000:
# 		break

# for prime in primes():
# 	print prime
# 	if prime >= 10000:
# 		break

def test_conjecture(i):
	for square in squares():
		done = False
		if square >= i:
			raise Exception("The smallest odd composite that cannot we written as the sum of a prime and twice a squre is " + str(i))
		for prime in primes():
			if prime + (2*square) == i:
				print '{} = {} + 2 x {}'.format(i, prime, square)
				done = True
				break
			elif prime + (2*square) > i:
				break
		if done:
			break

def run():
	composite_odds = []
	i = 7
	while i < 100000:
		i += 2
		if is_prime(i):
			continue
		else:
			composite_odds.append(i)
	pool = Pool(4)
	pool.map(test_conjecture, composite_odds)
	pool.close()
	pool.join()


# def run():
# 	not_done = True
# 	i = 7
# 	while i < 3000:
# 		i += 2
# 		if is_prime(i):
# 			continue
# 		else:
# 			for square in squares():
# 				done = False
# 				if square >= i:
# 					not_done = False
# 					result = i
# 					break
# 				for prime in primes():
# 					if prime + (2*square) == i:
# 						print '{} = {} + 2 x {}'.format(i, prime, square)
# 						done = True
# 						break
# 					elif prime + (2*square) > i:
# 						break
# 				if done:
# 					break

# print "The smallest odd composite that cannot we written as the sum of a prime and twice a squre is " + str(result)

from timeit import Timer
t = Timer(lambda: run())
print t.timeit(number=1)
