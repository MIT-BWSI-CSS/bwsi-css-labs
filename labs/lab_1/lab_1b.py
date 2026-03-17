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


def get_float(prompt: str) -> float:
    """
    Keeps asking the user for a number until they enter a valid one.

    Args:
        prompt (str): The message to display to the user.

    Returns:
        float: A valid float entered by the user.
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def get_operation(prompt: str) -> str:
    """
    Keeps asking the user for an operation until they enter a valid one.

    Args:
        prompt (str): The message to display to the user.

    Returns:
        str: A valid operation string.
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

    # Ask the user for valid numeric input
    num1 = get_float("Enter the first number: ")
    num2 = get_float("Enter the second number: ")

    # Ask the user for a valid operation
    operation = get_operation("Enter the operation (add, subtract, multiply, divide): ")

    # Handle divide by zero gracefully
    try:
        result = simple_calculator(operation, num1, num2)
        print(f"The result of {operation}ing {num1} and {num2} is: {result}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()