import unittest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from pricing import apply_discount, add_tax, checkout_total


class PricingTests(unittest.TestCase):
    def test_discount_is_percentage(self):
        self.assertEqual(apply_discount(200.0, 10), 180.0)

    def test_zero_discount(self):
        self.assertEqual(apply_discount(99.99, 0), 99.99)

    def test_invalid_discount(self):
        with self.assertRaises(ValueError):
            apply_discount(100.0, 150)

    def test_tax(self):
        self.assertEqual(add_tax(100.0, 0.08), 108.0)

    def test_checkout_total(self):
        # 200 - 10% = 180, + 8% tax = 194.40
        self.assertEqual(checkout_total(200.0, 10, 0.08), 194.4)


if __name__ == "__main__":
    unittest.main()
