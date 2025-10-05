a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("\nAddition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)

if b != 0:
    print("Division:", a / b)
else:
    print("Division: Not possible (cannot divide by zero)")
