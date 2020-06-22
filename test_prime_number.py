import prime_number
import unittest

class TestPrimeNumber(unittest.TestCase):

    number = prime_number.PrimeNumber()

    def test_two_returns_two(self):
        self.assertEqual([2], self.number.factorize(2))

    def test_three_returns_three(self):
        self.assertEqual([3], self.number.factorize((3)))

    def test_four_returns_two_two(self):
        self.assertEqual([2, 2], self.number.factorize(4))

    def test_five_returns_five(self):
        self.assertEqual([5], self.number.factorize(5))

    def test_six_returns_two_three(self):
        self.assertEqual([2, 3], self.number.factorize(6))

    def test_twenty_one_returns_three_seven(self):
        self.assertEqual([2, 3], self.number.factorize(6))

if __name__ == "__main__":
    unittest.main()