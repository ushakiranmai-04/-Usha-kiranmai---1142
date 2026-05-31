# Attendance Calculator

attended = int(input("Classes Attended: "))
total = int(input("Total Classes Conducted: "))
target = float(input("Required Attendance Percentage: "))

attendance = (attended / total) * 100

print(f"\nCurrent Attendance = {attendance:.2f}%")

if attendance >= target:
    print("Attendance Requirement Met")
else:
    future_classes = 0

    while ((attended + future_classes) /
           (total + future_classes)) * 100 < target:
        future_classes += 1

    print("Attendance Requirement Not Met")
    print("Classes to Attend Continuously:", future_classes)