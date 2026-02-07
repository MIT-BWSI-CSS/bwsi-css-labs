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

def sanitized_float(prompt = "Enter a number...") -> float:
    """
    Requests sanitized float from the user. Returns said float when it resolves
    """
    while True:
        try:
            x = float(input(prompt))
            return x
        except ValueError:
            print("Invalid input, please try again.")

def sanitized_operation(prompt = "Enter the operation (add, subtract, multiply, divide): ", valid_set = set()) -> str:
    """
    Returns sanitized string from valid_set to the user.
    
    :param prompt: Prompt to display to the user
    :param valid_set: Valid set of strings to accept.
    :return: String given by user out of set options.
    :rtype: str
    """
    while True:
        try:
            x = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()
            if x not in valid_set: raise Exception("Input not part of valid set") # invalid input
            return x
        except Exception:
            print("Invalid input, please try again.")


def main():
    
    print(f"===== Simple Calculator =====")

    # Ask the user for sample input    
    num1 = sanitized_float("Enter the first number: ")
    num2 = sanitized_float("Enter the second number: ")
    operation = sanitized_operation("Enter the operation (add, subtract, multiply, divide): ", {"add", "subtract", "multiply", "divide"})

    # Perform the calculation and display the result
    result = simple_calculator(operation, num1, num2)
    print(f"The result of {operation}ing {num1} and {num2} is: {result}")


if __name__ == "__main__":
    main()
