# Enhanced Loan Eligibility System

age = int(input("Enter age: "))
salary = int(input("Enter monthly salary: "))
employment = input("Enter employment type (salaried/self-employed): ").lower()

if age < 21 or age > 60:
    print("Rejected: Age must be between 21 and 60")
elif salary < 25000:
    print("Rejected: Salary must be at least ₹25,000")
elif age >= 21 and age <= 30 and salary < 30000:
    print("Needs guarantor")
elif age > 55 and employment == "self-employed":
    print("High risk, senior review needed")
else:
    print("Approved")