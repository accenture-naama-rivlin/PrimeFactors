import prime_number
import unittest

class TestPrimeNumber(unittest.TestCase):

    def test_two_returns_two(self):
        number = prime_number.PrimeNumber()
        self.assertEqual([2], number.factorize(2))

if __name__ == "__main__":
    unittest.main()