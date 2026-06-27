# exceptions.py

"""
This file contains custom exceptions for Secure Calculator Pro.
"""

class InvalidNumberError(Exception):
    """Raised when the user enters an invalid number."""
    pass


class DivisionByZeroError(Exception):
    """Raised when division by zero is attempted."""
    pass