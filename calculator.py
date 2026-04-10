# Simple Calculator
# Author: Yusuf Soylu
# A beginner Python project — performs basic math operations

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b


def calculator():
    print("==========================")
    print("   Simple Calculator 🧮   ")
    print("==========================")
    print("Operations:")
    print("  1 — Addition       (+)")
    print("  2 — Subtraction    (-)")
    print("  3 — Multiplication (x)")
    print("  4 — Division       (/)")
    print("  5 — Quit")
    print("--------------------------")

    while True:
        choice = input("\nChoose an operation (1/2/3/4/5): ")

        if choice == "5":
            print("Goodbye! 👋")
            break

        if choice not in ("1", "2", "3", "4"):
            print("Invalid choice. Please enter a number between 1 and 5.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            continue

        if choice == "1":
            print(f"Result: {num1} + {num2} = {add(num1, num2)}")
        elif choice == "2":
            print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
        elif choice == "3":
            print(f"Result: {num1} x {num2} = {multiply(num1, num2)}")
        elif choice == "4":
            print(f"Result: {num1} / {num2} = {divide(num1, num2)}")


calculator()
