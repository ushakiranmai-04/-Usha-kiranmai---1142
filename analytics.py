# analytics.py

"""
This file generates analytics for Secure Calculator Pro.
"""

from collections import Counter


def generate_report():
    """
    Generates analytics report.
    """

    # ---------- Total Calculations ----------
    try:
        with open("history.txt", "r") as file:
            calculations = file.readlines()
            total_calculations = len(calculations)

    except FileNotFoundError:
        total_calculations = 0

    # ---------- Total Errors ----------
    try:
        with open("error.log", "r") as file:
            errors = file.readlines()

            error_lines = []

            for line in errors:
                if "ERROR" in line:
                    error_lines.append(line)

            total_errors = len(error_lines)

            error_types = []

            for line in error_lines:
                message = line.split("ERROR - ")[-1].strip()
                error_types.append(message)

            if error_types:
                most_common_error = Counter(error_types).most_common(1)[0][0]
            else:
                most_common_error = "No Errors"

    except FileNotFoundError:
        total_errors = 0
        most_common_error = "No Errors"

    print("\n========== Analytics Report ==========")
    print("Total Calculations :", total_calculations)
    print("Total Errors       :", total_errors)
    print("Most Common Error  :", most_common_error)
    print("======================================")