import prime_number
import unittest

class TestPrimeNumber(unittest.TestCase):

    number = prime_number.PrimeNumber()

    def test_two_returns_two(self):
        self.assertEqual([2], self.number.factorize(2))

    def test_three_returns_three(self):
        self.assertEqual([3], self.number.factorize((3)))

if __name__ == "__main__":
    unittest.main()