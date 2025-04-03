import unittest
from week3exercises import pairwise_digits
from week3exercises import is_valid_password

class TestFunctions(unittest.TestCase):
    def test_pairwise(self):
        self.assertEqual(pairwise_digits("1234", "1234"), "[1, 1, 1, 1]")
        self.assertEqual(pairwise_digits("1234", "9876"), "[0, 0, 0, 0]")
        self.assertEqual(pairwise_digits("281", "681"), "[0, 1, 1]")
        self.assertEqual(pairwise_digits("1234567", "1234"), "[1, 1, 1, 1, 0, 0, 0]")
    def test_password(self):
        self.assertEqual(is_valid_password("Password"), False)
        self.assertEqual(is_valid_password("Password1"), True)
        self.assertEqual(is_valid_password("password1"), False)
        self.assertEqual(is_valid_password("PASSWORD"), False)

if __name__ == "__main__":
    unittest.main()