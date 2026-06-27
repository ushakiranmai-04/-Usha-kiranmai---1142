from calculator import Calculator
from exceptions import InvalidNumberError, DivisionByZeroError
from logger import log_error
from analytics import generate_report

calculator = Calculator()


def view_history():
    try:
        with open("history.txt", "r") as file:
            print("\n===== Calculation History =====")
            data = file.read()

            if data:
                print(data)
            else:
                print("No calculations found.")

    except FileNotFoundError:
        print("History file not found.")


def view_error_report():
    try:
        with open("error.log", "r") as file:
            print("\n===== Error Report =====")
            data = file.read()

            if data:
                print(data)
            else:
                print("No errors found.")

    except FileNotFoundError:
        print("Error log not found.")


while True:

    print("\n========== Secure Calculator Pro ==========")
    print("1. Perform Calculation")
    print("2. View Calculation History")
    print("3. View Error Report")
    print("4. Analytics Report")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        print("\nChoose Operation")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        operation = input("Enter operation: ")

        try:

            num1 = input("Enter first number: ")
            num2 = input("Enter second number: ")

            try:
                num1 = float(num1)
                num2 = float(num2)

            except ValueError:
                raise InvalidNumberError("Please enter valid numbers.")

            if operation == "1":
                result = calculator.add(num1, num2)

            elif operation == "2":
                result = calculator.subtract(num1, num2)

            elif operation == "3":
                result = calculator.multiply(num1, num2)

            elif operation == "4":
                result = calculator.divide(num1, num2)

            else:
                print("Invalid operation.")
                continue

            print("Result =", result)
        except InvalidNumberError as e:
            print(e)
            log_error(str(e))

        except DivisionByZeroError as e:
            print(e)
            log_error(str(e))

        except Exception as e:
            print("Unexpected Error:", e)
            log_error(str(e))

        else:
            print("Calculation completed successfully.")

        finally:
            print("Thank you for using Secure Calculator Pro.")

    elif choice == "2":
        view_history()

    elif choice == "3":
        view_error_report()

    elif choice == "4":
        generate_report()

    elif choice == "5":
        print("Thank you for using Secure Calculator Pro.")
        break

    else:
        print("Invalid menu choice. Please try again.")