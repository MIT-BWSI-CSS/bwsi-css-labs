"""
lab_1b.py

This is a script that implements a simple calculator. It takes two numbers and an operation,
then performs the operation and returns the result. 

The script asks the user to input the numbers and the operation to be performed,
and prints the result to the terminal window.

"""

from sqlalchemy import false


def simple_calculator(operation: str, num1: float, num2: float) -> float:
    """
    Function that takes in two numbers and an operation (add, subtract, multiply, divide),
    then performs the operation on the two numbers and returns the result.

    Args:
        operation (str): The operation to perform ("add", "subtract", "multiply", "divide").
        num1 (float): The first number.
        num2 (float): The second number.

    Returns:
        float: The result of the operation.
    """

    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 != 0:
            return num1 / num2
        else:
            raise ValueError("Cannot divide by zero.")
    else:
        raise ValueError("Invalid operation. Please choose from 'add', 'subtract', 'multiply', or 'divide'.")

def main():
    print("===== Simple Calculator =====")
    
    # Loop indefinitely until we reach the 'break' statement
    while True:           
        try:
            # 1. Get Numbers
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            
            # 2. Get Operation
            operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()
            
            # 3. Attempt Calculation
            # We call this inside the try block to catch "divide by zero" or "invalid operation"
            result = simple_calculator(operation, num1, num2)
            
            # 4. Success! Print and exit the loop
            print(f"\nThe result of {operation}ing {num1} and {num2} is: {result}")
            break 
            
        except ValueError as e:
            # This catches both non-numeric inputs and our custom errors from the function
            print(f"\n[Error]: {e}")
            print("Please try again.\n")

if __name__ == "__main__":
    main()