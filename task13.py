import csv

# Step 1: Create and write data to student.csv
students = [
    [101, "Rahul", 85, 90, 88, 92],
    [102, "Priya", 78, 82, 80, 85],
    [103, "Amit", 90, 95, 93, 97],
    [104, "Sneha", 88, 84, 86, 89],
    [105, "Kiran", 75, 70, 72, 78],
    [106, "Anjali", 92, 91, 94, 90],
    [107, "Ravi", 68, 72, 70, 74],
    [108, "Meena", 81, 83, 85, 80],
    [109, "Vijay", 87, 89, 90, 88],
    [110, "Pooja", 95, 96, 94, 98]
]

with open("student.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Roll No", "Name", "Maths", "Science", "English", "Computer"])
    writer.writerows(students)

print("student.csv created successfully!\n")

# Step 2: Read and display all student records
print("Student Records:")
with open("student.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# Step 3: Find student with highest marks
highest_student = ""
highest_total = 0

with open("student.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        total = int(row["Maths"]) + int(row["Science"]) + int(row["English"]) + int(row["Computer"])

        if total > highest_total:
            highest_total = total
            highest_student = row["Name"]

print("\nStudent with Highest Marks:")
print("Name:", highest_student)
print("Total Marks:", highest_total)

# Step 4: Calculate average marks of all students
total_marks_all = 0
student_count = 0

with open("student.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        total = int(row["Maths"]) + int(row["Science"]) + int(row["English"]) + int(row["Computer"])
        total_marks_all += total
        student_count += 1

average_marks = total_marks_all / student_count

print("\nAverage Marks of All Students:", average_marks)