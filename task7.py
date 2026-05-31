# EMI Calculator

principal = float(input("Enter Loan Amount: "))
rate = float(input("Enter Annual Interest Rate (%): "))
years = int(input("Enter Loan Tenure (Years): "))

monthly_rate = rate / (12 * 100)
months = years * 12

emi = (principal * monthly_rate * (1 + monthly_rate) ** months) / ((1 + monthly_rate) ** months - 1)

print(f"\nMonthly EMI = ₹{emi:.2f}")