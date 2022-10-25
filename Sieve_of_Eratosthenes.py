
def SieveOfEratosthenes(num):
	prime = [True for i in range(num+1)]
	p = 2
	while (p * p <= num):

		if (prime[p] == True):

			for i in range(p * p, num+1, p):
				prime[i] = False
		p += 1

	for p in range(2, num+1):
		if prime[p]:
			print(p)

if __name__ == '__main__':
	num = 50
	print("Following are the prime numbers smaller"),
	print("than or equal to", num)
	SieveOfEratosthenes(num)
