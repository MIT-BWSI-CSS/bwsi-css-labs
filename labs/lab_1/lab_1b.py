"""
lab_1b.py

This is a script that implements a simple calculator. It takes two numbers and an operation,
then performs the operation and returns the result. 

The script asks the user to input the numbers and the operation to be performed,
and prints the result to the terminal window.

"""

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
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        raise ValueError("Invalid input. Please enter a valid number.")
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


def request_sanitized_number(prompt: str) -> float:
    """
    Function to request a number from the user and ensure that it is a valid float.

    """
    while True:
        try:
            number = float(input(prompt))
            return number
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def request_sanitized_operation(prompt: str) -> str:
    """
    Function to request an operation from the user and ensure that it is valid.

    """
    valid_operations = {"add", "subtract", "multiply", "divide"}
    while True:
        operation = input(prompt).strip().lower()
        if operation in valid_operations:
            return operation
        else:
            print("Invalid operation. Please choose from 'add', 'subtract', 'multiply', or 'divide'.")

def main():
    
    print(f"===== Simple Calculator =====")

    # Ask the user for sample input    
    num1 = request_sanitized_number("Enter the first number: ")
    num2 = request_sanitized_number("Enter the second number: ")
    operation = request_sanitized_operation("Enter the operation (add, subtract, multiply, divide): ")

    # Perform the calculation and display the result
    result = simple_calculator(operation, num1, num2)
    print(f"The result of {operation}ing {num1} and {num2} is: {result}")


if __name__ == "__main__":
    main()
