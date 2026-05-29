# =========================
# Task 2 — Smart Bill Splitter
# =========================

# Taking inputs
bill_amount = float(input("Enter total bill amount: "))
people = int(input("Enter number of people: "))
tip_percentage = float(input("Enter tip percentage: "))

# Calculating tip amount
tip_amount = (bill_amount * tip_percentage) / 100

# Total bill after adding tip
total_bill = bill_amount + tip_amount

# Amount per person
amount_per_person = total_bill / people

# Printing summary
print("\n===== BILL SUMMARY =====")
print(f"Original Bill      : ₹{round(bill_amount, 2)}")
print(f"Tip Amount         : ₹{round(tip_amount, 2)}")
print(f"Total Bill         : ₹{round(total_bill, 2)}")
print(f"Amount Per Person  : ₹{round(amount_per_person, 2)}")
print("========================")