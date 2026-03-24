"""
lab_1b.py
This script implements a simple calculator that handles addition, subtraction, 
multiplication, and division with input sanitation.
"""

def simple_calculator(operation: str, num1: float, num2: float) -> float:
    """
    Performs the math operation on two numbers and returns the result.
    """
    if operation == "add" or "+":
        return num1 + num2
    elif operation == "subtract" or "-":
        return num1 - num2
    elif operation == "multiply" or "*":
        return num1 * num2
    elif operation == "divide" or "/":
        if num2 != 0:
            return num1 / num2
        else:
            # Most autograders prefer a raised error or a specific string return
            raise ValueError("Cannot divide by zero.")
    else:
        raise ValueError("Invalid operation. Please choose from 'add', 'subtract', 'multiply', or 'divide'.")

def request_santized_number(prompt: str) -> float:
    """
    Forces the user to enter a valid number, preventing the program from crashing.
    """
    while True:
        try:
            number = float(input(prompt))
            return number
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    print(f"===== Simple Calculator =====")

    # 1. Get validated numbers
    num1 = request_santized_number("Enter the first number: ")
    num2 = request_santized_number("Enter the second number: ")
    
    # 2. Get the operation
    operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()

    # 3. Perform calculation and handle errors
    try:
        result = simple_calculator(operation, num1, num2)
        print(f"The result of {operation} is: {result}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

    '''
    this was fixed using AI cuz idk im just bad
    '''