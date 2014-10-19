from utils import is_prime, primes

consecutive_primes = []
total = 0
for prime in primes():
	total += prime
	if is_prime(total):
		consecutive_primes.append(prime)
	else:
		break
print consecutive_primes
