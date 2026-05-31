n = int(input("Enter n: "))

print("\n1. Right Triangle Pattern")
for i in range(1, n + 1):
    print("*" * i)

print("\n2. Inverted Triangle Pattern")
for i in range(n, 0, -1):
    print("*" * i)

print("\n3. Pascal's Triangle")
for i in range(n):
    num = 1
    for j in range(i + 1):
        print(num, end=" ")
        num = num * (i - j) // (j + 1)
    print()

print("\n4. Prime Numbers up to", n)
for num in range(2, n + 1):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num, end=" ")