# test_calculator.py

import unittest
from calculator import Calculator
import json


class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(Calculator.add(2, 3), 5)
        self.assertEqual(Calculator.add(-1, 1), 0)
        self.assertEqual(Calculator.add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(Calculator.subtract(10, 5), 5)
        self.assertEqual(Calculator.subtract(0, 0), 0)
        self.assertEqual(Calculator.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(Calculator.multiply(4, 3), 12)
        self.assertEqual(Calculator.multiply(-2, 2), -4)
        self.assertEqual(Calculator.multiply(0, 10), 0)

    def test_divide(self):
        self.assertEqual(Calculator.divide(10, 2), 5)
        self.assertEqual(Calculator.divide(-6, 3), -2)
        with self.assertRaises(ValueError):
            Calculator.divide(10, 0)


if __name__ == "__main__":
    # Run tests
    test_result = unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestCalculator))

    # Collect test results
    results = {
        "total_tests": test_result.testsRun,
        "failures": len(test_result.failures),
        "errors": len(test_result.errors),
        "success": test_result.testsRun - len(test_result.failures) - len(test_result.errors)
    }

    # Write results to a file
    with open("test_results.json", "w") as result_file:
        json.dump(results, result_file)
