# ------------- Lesson 01 Functions - Solutions 1 -------------

# 1. Write a function called 'is_even' that takes a number as an argument and returns True if the number is even, and False otherwise.

from unittest import TestCase, main


def is_even(number):
    """
    Check if a number is even.
    """
    return number % 2 == 0

# 2. Write a function called 'is_odd' that takes a number as an argument and returns True if the number is odd, and False otherwise.
# You should use the is_even function to implement the is_odd function.


def is_odd(number):
    """
    Check if a number is odd.
    """
    return not is_even(number)


# 3. Write a function called 'evens_under' that takes a number as an argument and returns a list of all even numbers less than that number.

def evens_under(number):
    """
    Return a list of all even numbers less than the given number.
    """
    return [i for i in range(number) if is_even(i)]

# 4. Write a function called 'primes' that takes a number as an argument and returns a list of all prime numbers less than that number.


def is_prime(n):
    """
    Check if a number is prime.
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def primes(n):
    """
    Return a list of all prime numbers less than the given number.
    """
    return [i for i in range(n) if is_prime(i)]


# ------------------ Test cases ------------------

# Test the is_even function

class TestIsEven(TestCase):
    def test_is_even(self):
        self.assertTrue(is_even(2))
        self.assertTrue(is_even(0))
        self.assertFalse(is_even(3))
        self.assertFalse(is_even(-1))

# Test the is_odd function


class TestIsOdd(TestCase):
    def test_is_odd(self):
        self.assertTrue(is_odd(3))
        self.assertTrue(is_odd(-1))
        self.assertFalse(is_odd(2))
        self.assertFalse(is_odd(0))

# Test the evens_under function


class TestEvensUnder(TestCase):
    def test_evens_under(self):
        self.assertEqual(evens_under(10), [0, 2, 4, 6, 8])
        self.assertEqual(evens_under(5), [0, 2, 4])
        self.assertEqual(evens_under(0), [])
        self.assertEqual(evens_under(-5), [])

# Test the primes function


class TestPrimes(TestCase):
    def test_primes(self):
        self.assertEqual(primes(10), [2, 3, 5, 7])
        self.assertEqual(primes(20), [2, 3, 5, 7, 11, 13, 17, 19])
        self.assertEqual(primes(1), [])
        self.assertEqual(primes(0), [])
        self.assertEqual(primes(-5), [])


if __name__ == "__main__":
    main()

