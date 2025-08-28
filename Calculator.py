# calculator.py

def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

print("Simple Calculator")
print("1: Add, 2: Subtract, 3: Multiply, 4: Divide")

choice = input("Enter choice: ")
a = float(input("First number: "))
b = float(input("Second number: "))

if choice == "1":
    print("Result:", add(a, b))
elif choice == "2":
    print("Result:", subtract(a, b))
elif choice == "3":
    print("Result:", multiply(a, b))
elif choice == "4":
    print("Result:", divide(a, b))
else:
    print("Invalid choice")
