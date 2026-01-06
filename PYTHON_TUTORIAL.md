# Python Tutorial for Beginners

Welcome to this step-by-step Python tutorial! We'll start from the basics and build up to a working calculator.

---

## Step 1: Hello World

Let's start with the classic "Hello World" program.

**Create the file: `step1_hello.py`**

```python
print("Hello World!")
```

**Run the program:**
```bash
python step1_hello.py
```

---

## Step 2: Variables and Input

Now we'll learn about variables and how to receive input from the user.

**Create the file: `step2_variables.py`**

```python
# Variables
name = "Python"
age = 30

print(f"Hi, my name is {name} and I'm {age} years old!")

# Get input from the user
username = input("What's your name? ")
print(f"Hello {username}! Nice to meet you!")
```

---

## Step 3: Basic Calculations

Let's learn how to perform mathematical calculations.

**Create the file: `step3_calculations.py`**

```python
# Basic math
a = 10
b = 5

sum_result = a + b
difference = a - b
product = a * b
quotient = a / b

print(f"Sum: {a} + {b} = {sum_result}")
print(f"Difference: {a} - {b} = {difference}")
print(f"Product: {a} * {b} = {product}")
print(f"Quotient: {a} / {b} = {quotient}")

# With user input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print(f"{num1} + {num2} = {num1 + num2}")
```

---

## Step 4: Functions

Functions let us organize code and reuse it.

**Create the file: `step4_functions.py`**

```python
# Simple function
def greet():
    print("Hello from the function!")

# Function with parameters
def greet_person(name):
    print(f"Hello {name}!")

# Function that returns a value
def add(a, b):
    return a + b

# Use the functions
greet()
greet_person("Anna")
result = add(5, 3)
print(f"5 + 3 = {result}")
```

---

## Step 5: If Statements and Loops

Let's learn how to make decisions and repeat things.

**Create the file: `step5_control.py`**

```python
# If statements
age = int(input("How old are you? "))

if age >= 18:
    print("You are an adult!")
else:
    print("You are a minor!")

# Loops
print("\nCounting from 1 to 5:")
for i in range(1, 6):
    print(i)

# While loop
counter = 0
while counter < 3:
    print(f"Counter: {counter}")
    counter += 1
```

---

## Step 6: Multiple Files and Modules

Now we'll learn how to organize code into multiple files.

**Create the file: `math_functions.py`**

```python
def add(a, b):
    """Adds two numbers"""
    return a + b

def subtract(a, b):
    """Subtracts two numbers"""
    return a - b

def multiply(a, b):
    """Multiplies two numbers"""
    return a * b

def divide(a, b):
    """Divides two numbers"""
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b
```

**Create the file: `step6_modules.py`**

```python
# Import functions from math_functions.py
from math_functions import add, subtract, multiply, divide

# Use the functions
print(f"10 + 5 = {add(10, 5)}")
print(f"10 - 5 = {subtract(10, 5)}")
print(f"10 * 5 = {multiply(10, 5)}")
print(f"10 / 5 = {divide(10, 5)}")
```

---

## Step 7: A Simple Calculator

Now we'll build a complete calculator with multiple files!

**Create the file: `calculator_functions.py`**

```python
"""
Module with mathematical functions for the calculator
"""

def add(a, b):
    """Adds two numbers"""
    return a + b

def subtract(a, b):
    """Subtracts two numbers"""
    return a - b

def multiply(a, b):
    """Multiplies two numbers"""
    return a * b

def divide(a, b):
    """Divides two numbers"""
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

def power(a, b):
    """Calculates a raised to the power of b"""
    return a ** b
```

**Create the file: `calculator_ui.py`**

```python
"""
Module for the calculator's user interface
"""

def show_menu():
    """Displays the main menu"""
    print("\n" + "="*40)
    print("WELCOME TO THE CALCULATOR")
    print("="*40)
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (^)")
    print("0. Exit")
    print("="*40)

def get_number(prompt):
    """Gets a number from the user"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error: Please enter a valid number!")

def show_result(operation, num1, num2, result):
    """Displays the result of a calculation"""
    print(f"\n{num1} {operation} {num2} = {result}")
```

**Create the file: `calculator.py`**

```python
"""
Main program for the calculator
"""

from calculator_functions import add, subtract, multiply, divide, power
from calculator_ui import show_menu, get_number, show_result

def main():
    """Main function that runs the calculator"""
    while True:
        show_menu()
        choice = input("\nChoose an operation (0-5): ")
        
        if choice == "0":
            print("Thank you for using the calculator! Goodbye!")
            break
        
        if choice not in ["1", "2", "3", "4", "5"]:
            print("Invalid choice! Please try again.")
            continue
        
        # Get numbers from the user
        num1 = get_number("Enter the first number: ")
        num2 = get_number("Enter the second number: ")
        
        # Perform the calculation
        try:
            if choice == "1":
                result = add(num1, num2)
                show_result("+", num1, num2, result)
            elif choice == "2":
                result = subtract(num1, num2)
                show_result("-", num1, num2, result)
            elif choice == "3":
                result = multiply(num1, num2)
                show_result("*", num1, num2, result)
            elif choice == "4":
                result = divide(num1, num2)
                show_result("/", num1, num2, result)
            elif choice == "5":
                result = power(num1, num2)
                show_result("^", num1, num2, result)
        except ValueError as e:
            print(f"Error: {e}")
        
        # Ask if the user wants to continue
        continue_calc = input("\nDo you want to do another calculation? (y/n): ")
        if continue_calc.lower() != "y":
            print("Thank you for using the calculator! Goodbye!")
            break

if __name__ == "__main__":
    main()
```

---

## How to Run the Calculator

1. Make sure all three files are in the same folder:
   - `calculator_functions.py`
   - `calculator_ui.py`
   - `calculator.py`

2. Run the main program:
```bash
python calculator.py
```

---

## Summary

You have now learned:
- ✅ How to write and run Python programs
- ✅ Variables and input
- ✅ Basic mathematics
- ✅ Functions
- ✅ If statements and loops
- ✅ How to organize code into multiple files
- ✅ How to build a complete program (calculator)

## Next Steps

Now you can:
- Experiment with the code
- Add more functions (e.g., square root, sine, etc.)
- Improve the user interface
- Add error handling
- Save calculations to a file

Good luck with your Python programming! 🐍

