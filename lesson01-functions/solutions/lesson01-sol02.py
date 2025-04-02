
# ------------- Lesson 01 Functions - Solution 2 -------------


# 1. Extend the below code to include the following:
#    - Check whether the paassword has at least one uppercase letter.
#    - Check whether the password has at least one lowercase letter.
#    - Check whether the password has at least one digit.
#    - Check whether the password has at least one special character (within this list !@?$%^&*).
# Hint: You can use the built in any, char.isupper, char.islower, and char.isdigit functions to check for these conditions.

from unittest import TestCase, main


def has_uppercase(password):
    """Check if the password contains at least one uppercase letter."""
    return any(char.isupper() for char in password)


def has_lowercase(password):
    """Check if the password contains at least one lowercase letter."""
    return any(char.islower() for char in password)


def has_digit(password):
    """Check if the password contains at least one digit."""
    return any(char.isdigit() for char in password)


def has_special_char(password):
    """Check if the password contains at least one special character."""
    special_chars = "!@?$%^&*"
    return any(char in special_chars for char in password)


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

    if not has_uppercase(password):
        return False
    if not has_lowercase(password):
        return False
    if not has_digit(password):
        return False
    if not has_special_char(password):
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

