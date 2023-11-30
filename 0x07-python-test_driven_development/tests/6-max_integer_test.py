#!/usr/bin/python3
"""Unittest for max_integer([...])
"""


import unittest
max_integer = __import__("6-max_integer").max_integer

class TestMaxInteger(unittest.TestCase):
    def test_regular_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([100]), 100)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_floats(self):
        self.assertEqual(max_integer([1.5, 2.7, 3.1]), 3.1)
        self.assertEqual(max_integer([-1.5, -2.7, -3.1]), -1.5)

    def test_mixed_list(self):
        self.assertEqual(max_integer([1, 2.5, 3, 4]), 4)
        self.assertEqual(max_integer([-1, -2.5, -3, -4]), -1)
        self.assertEqual(max_integer([-1, 2.5, 3, 4]), 4)

if __name__ == "__main__":
    unittest.main()
