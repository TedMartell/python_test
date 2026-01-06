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

