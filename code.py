"""
This module contains utility functions for mathematical operations.
"""

"""
This module contains utility functions for mathematical operations.
"""

def calculator():
    """
    Brief description of what the function does.

    Args:
        No arguments are required for this function.

    Returns:
        type: returns the calculated result
    """
    print("Welcome to the Python Calculator!")
    print("Select operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (*)")

    while True:
        choice = input("Enter choice (1/2/3/4): ")

        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == '1':
                    print(f"The result is: {num1 + num2}")
                elif choice == '2':
                    print(f"The result is: {num1 - num2}")
                elif choice == '3':
                    print(f"The result is: {num1 * num2}")
                elif choice == '4':
                    if num2 != 0:
                        print(f"The result is: {num1 / num2}")
                    else:
                        print("Error: Division by zero is not allowed.")

            except ValueError:
                print("Invalid input. Please enter numerical values.")
        else:
            print("Invalid choice. Please select a valid operation.")

        next_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if next_calculation.lower() != 'yes':
            print("Thank you for using the calculator!")
            break

calculator()
