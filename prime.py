def primes(n):
	"""
	function for calculating prime numbers with O(n^2) time complexity
	"""
	if not isinstance(n, int):
		return "only integers allowed"
	if n == 1 or n == 0:
		return []
	if n == 2:
		return [2]
	if n < 0:
		return "primes are greater than 1"
	prime_list = [2, 3]
	if n <= 3:
		return prime_list
	for i in range(4, n+1):
		prime_flag = True
		for prime in prime_list:
			if i % prime == 0:
				prime_flag = False
		if prime_flag:
			prime_list.append(i)
	return prime_list