# tests/test_calculator.py

# ISSUE: This file is intentionally left mostly empty or with very few tests
# to demonstrate the need for a comprehensive test suite.
# An AI agent could be prompted to "Generate comprehensive unit tests for calculator.py"

import unittest
from calculator import add

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)

    # TODO: Add tests for subtract, multiply, divide, and factorial functions.
    # Specifically, test edge cases and error handling for divide (by zero)
    # and factorial (negative numbers, large numbers).

if __name__ == '__main__':
    unittest.main()
