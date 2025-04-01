# ------------- Lesson 01 Functions - Exercise 2 -------------


# 1. Extend the below code to include the following:
#    - Check whether the paassword has at least one uppercase letter.
#    - Check whether the password has at least one lowercase letter.
#    - Check whether the password has at least one digit.
#    - Check whether the password has at least one special character (within this list !@?$%^&*).
# Hint: You can use the built in any, char.isupper, char.islower, and char.isdigit functions to check for these conditions.

from unittest import TestCase, main


def is_valid_password(password):
    """
    Check if the password is valid based on the following criteria:
    - At least 8 characters long
    - At least one uppercase letter
    - At least one lowercase letter
    - At least one digit
    - At least one special character
    """
    if len(password) < 8:
        return False

    # If all checks pass, the password is valid
    return True


# ------------------ Test cases ------------------


# Test the is_valid_password function


class TestIsValidPassword(TestCase):
    def test_is_valid_password(self):
        self.assertTrue(is_valid_password("Password123!"))
        self.assertFalse(is_valid_password("short"))
        self.assertFalse(is_valid_password("NoSpecialChar1"))
        self.assertFalse(is_valid_password("NOLOWERCASE1!"))
        self.assertFalse(is_valid_password("nouppercase1!"))
        self.assertFalse(is_valid_password("NoDigit!"))
        self.assertFalse(is_valid_password("12345678"))
        self.assertFalse(is_valid_password("!@?$%^&*"))


if __name__ == "__main__":
    main()

