def primes(n):
	if not isinstance(n, int):
		return "only integers allowed"
	if n == 1 or n == 0:
		return []
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