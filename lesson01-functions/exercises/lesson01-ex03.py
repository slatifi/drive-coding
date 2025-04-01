# ------------- Lesson 01 Functions - Exercise 3 -------------


# 1. Rewrite the below lambda function to a regular function called custom_list. Include a docstring of the conditions.
# result = [(lambda x: x**2)(x) if (lambda y: y % 2 == 0)(x) else (lambda z: z + 1)(x) for x in range(10) if (lambda w: w > 3)(x)]
# Instead of limiting the range to 10, use a parameter n to limit the range of numbers.


# ------------------ Test cases ------------------

from unittest import TestCase, main


# Test the custom_list function
class TestCustomList(TestCase):
    def test_custom_list(self):
        self.assertEqual(custom_list(10), [16, 6, 36, 8, 64, 10])
        self.assertEqual(custom_list(6), [16, 6])
        self.assertEqual(custom_list(4), [])
        self.assertEqual(custom_list(0), [])
        self.assertEqual(custom_list(-5), [])


if __name__ == "__main__":
    main()

