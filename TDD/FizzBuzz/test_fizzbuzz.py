import unittest
from fizzbuzz import fizz_buzz

class TestFizzBuzz(unittest.TestCase):

    def test_non_divisible_numbers(self):
        self.assertEqual(fizz_buzz(1), "1")
        self.assertEqual(fizz_buzz(2), "2")
        self.assertEqual(fizz_buzz(7), "7")

    def test_divisible_by_3(self):
        self.assertEqual(fizz_buzz(3), "Fizz")
        self.assertEqual(fizz_buzz(6), "Fizz")
        self.assertEqual(fizz_buzz(9), "Fizz")

    def test_divisible_by_5(self):
        self.assertEqual(fizz_buzz(5), "Buzz")
        self.assertEqual(fizz_buzz(10), "Buzz")
        self.assertEqual(fizz_buzz(20), "Buzz")

    def test_divisible_by_3_and_5(self):
        self.assertEqual(fizz_buzz(15), "FizzBuzz")
        self.assertEqual(fizz_buzz(30), "FizzBuzz")
        self.assertEqual(fizz_buzz(45), "FizzBuzz")

if __name__ == '__main__':
    unittest.main()
