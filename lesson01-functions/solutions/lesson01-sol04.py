# ------------- Lesson 01 Functions - Solution 4 -------------

# 1. Write a recursive function called fibonacci that takes a number n as an argument and returns the nth Fibonacci number. The Fibonacci sequence is defined as follows:
#    - fibonacci(0) = 0
#    - fibonacci(1) = 1
#    - fibonacci(n) = sum of the two preceding fibonacci numbers for n > 1, e.g. fibonacci(2) = fibonacci(1) + fibonacci(0) = 1 & fibonacci(3) = fibonacci(2) + fibonacci(1) = 2

from unittest import TestCase, main


def fibonacci(n):
    """Returns the nth Fibonacci number."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# 2. Write a recursive function called reverse_array that takes an array as an argument and returns the array in reverse order.
# For example, reverse_array([1, 2, 3]) should return [3, 2, 1]. You can use slicing to reverse the array.


def reverse_array(arr):
    """Returns the array in reverse order."""
    if len(arr) == 0:
        return []
    else:
        return [arr[-1]] + reverse_array(arr[:-1])


# ------------------ Test cases ------------------


# Test the fibonacci function
class TestFibonacci(TestCase):
    def test_fibonacci(self):
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(2), 1)
        self.assertEqual(fibonacci(3), 2)
        self.assertEqual(fibonacci(10), 55)
        self.assertEqual(fibonacci(20), 6765)
        self.assertEqual(fibonacci(-10), 0)

# Test the reverse_array function


class TestReverseArray(TestCase):
    def test_reverse_array(self):
        self.assertEqual(reverse_array([1, 2, 3]), [3, 2, 1])
        self.assertEqual(reverse_array([1]), [1])
        self.assertEqual(reverse_array([]), [])
        self.assertEqual(reverse_array([1, 2, 3, 4]), [4, 3, 2, 1])


if __name__ == '__main__':
    main()

