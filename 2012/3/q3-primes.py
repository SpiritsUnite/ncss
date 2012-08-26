low, high = map(int, raw_input("Enter Numbers: ").split())
isPrime = [True] * (high + 1)
isPrime[0] = isPrime[1] = False
for i in xrange(len(isPrime)):
	if not isPrime[i]:
		continue
	for j in xrange(i + i, len(isPrime), i):
		isPrime[j] = False

primes = [i[0] for i in filter(lambda x: x[0] >= low and x[1], enumerate(isPrime))]
if primes:
	diffPrime = []
	for i in xrange(len(primes) - 1):
		diffPrime.append(primes[i + 1] - primes[i])
	
	index = sorted(enumerate(diffPrime), key=lambda x: x[1], reverse=True)[0][0]
	print ' '.join(map(str, primes[index:index+2]))