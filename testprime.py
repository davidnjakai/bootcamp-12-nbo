from prime import primes
import unittest

class TestPrime(unittest.TestCase):
	def test_validity(self):
		self.assertEqual(primes(10), [2, 3, 5, 7])

	def test_non_integers(self):
		self.assertEqual(primes("something"), "only integers allowed")

	def test_one_not_prime(self):
		self.assertEqual(primes(1), [])

	def test_two_returns_two(self):
		self.assertEqual(primes(2), [2])

	def test_zero_returns_empty_string(self):
		self.assertEqual(primes(0), [])

	def test_integers_less_than_zero(self):
		self.assertEqual(primes(-5), "primes are greater than 1")

if __name__ == '__main__':
	unittest.main()