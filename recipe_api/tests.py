from django.test import TestCase

from .calc import add, substract


class CalcTests(TestCase):
    def test_add_numbers(self):
        """Test that add two numbers"""
        self.assertEqual(add(3, 8), 11)

    def test_substract_numbers(self):
        """test that values are substracted and returned"""

        self.assertEqual(substract(7, 4), 3)
