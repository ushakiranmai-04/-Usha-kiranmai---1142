# 1. Create a list of 5 fruits and print all items
fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]

print("List of Fruits:")
for fruit in fruits:
    print(fruit)

# 2. Create a tuple of 3 colors and print the first color
colors = ("Red", "Green", "Blue")

print("\nTuple of Colors:")
print("First Color:", colors[0])

# 3. Create a dictionary with student names and marks
students = {
    "Rahul": 85,
    "Priya": 92,
    "Kiran": 78
}

print("\nStudent Marks:")
print(students)

# 4. Create a set of 5 numbers and print all unique values
numbers = {10, 20, 30, 20, 40, 10, 50}

print("\nUnique Numbers:")
print(numbers)

# 5. Create a dictionary of products and quantities
stock = {
    "Laptop": 10,
    "Mouse": 25,
    "Keyboard": 15,
    "Monitor": 8
}

print("\nStock Details:")
for product, quantity in stock.items():
    print(product, ":", quantity)