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

