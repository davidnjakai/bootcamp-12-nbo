from prime import primes
import unittest

class TestPrime(unittest.TestCase):
	def test_validity(self):
		self.assertEqual(primes(10), [2, 3, 5, 7])

if __name__ == '__main__':
	unittest.main()