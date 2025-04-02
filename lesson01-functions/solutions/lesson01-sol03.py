# ------------- Lesson 01 Functions - Solution 3 -------------


# 1. Rewrite the below lambda function to a regular function called custom_list. Include a docstring of the conditions.
# result = [(lambda x: x**2)(x) if (lambda y: y % 2 == 0)(x) else (lambda z: z + 1)(x) for x in range(10) if (lambda w: w > 3)(x)]
# Instead of limiting the range to 10, use a parameter n to limit the range of numbers.

from unittest import TestCase, main


def squared(x):
    """Returns the square of x."""
    return x ** 2


def is_even(x):
    """Checks if x is even."""
    return x % 2 == 0


def increment(x):
    """Increments x by 1."""
    return x + 1


def custom_list(n):
    """
    Generates a list of numbers based on the following conditions:
    - If the number is even, square it.
    - If the number is odd, increment it by 1.
    - Only loops over numbers greater than 3.

    Parameters:
        n (int): The upper limit for generating the list.

    Returns:
        list: A list of processed numbers based on the conditions above.
    """
    result = []
    for x in range(n):
        if x > 3:
            if is_even(x):
                result.append(squared(x))
            else:
                result.append(increment(x))
    return result


# ------------------ Test cases ------------------


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

