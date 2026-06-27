# calculator.py

"""
Calculator class for Secure Calculator Pro
Performs arithmetic operations and stores calculation history.
"""

from exceptions import DivisionByZeroError


class Calculator:
    """
    Calculator class that performs arithmetic operations.
    """

    def add(self, num1, num2):
        result = num1 + num2
        self.save_history(f"{num1} + {num2} = {result}")
        return result

    def subtract(self, num1, num2):
        result = num1 - num2
        self.save_history(f"{num1} - {num2} = {result}")
        return result

    def multiply(self, num1, num2):
        result = num1 * num2
        self.save_history(f"{num1} * {num2} = {result}")
        return result

    def divide(self, num1, num2):
        if num2 == 0:
            raise DivisionByZeroError("Cannot divide by zero.")

        result = num1 / num2
        self.save_history(f"{num1} / {num2} = {result}")
        return result

    def save_history(self, calculation):
        """
        Saves successful calculations to history.txt
        """
        with open("history.txt", "a") as file:
            file.write(calculation + "\n")