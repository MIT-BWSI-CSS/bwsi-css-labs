"""
lab_1b.py

This is a script that implements a simple calculator. It takes two numbers and an operation,
then performs the operation and returns the result. 

The script asks the user to input the numbers and the operation to be performed,
and prints the result to the terminal window.

test2
test3
test4
test5
test6
test7
"""
def request_sanitized_number(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

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
    
    print(f"===== Simple Calculator =====")

    # Ask the user for sample input    
    num1 = request_sanitized_number("Enter the first number: ")
    num2 = request_sanitized_number("Enter the second number: ")
    operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()

    # Perform the calculation and display the result
    result = simple_calculator(operation, num1, num2)
    print(f"The result of {operation}ing {num1} and {num2} is: {result}")


if __name__ == "__main__":
    main()
import pytest
from labs.lab_1.lab_1b import simple_calculator
def test_addition():
    assert simple_calculator("add", 5, 3) == 8
    assert simple_calculator("add", -2, 2) == 0
    assert simple_calculator("add", 0, 0) == 0

def test_subtraction():
    assert simple_calculator("subtract", 5, 3) == 2
    assert simple_calculator("subtract", -2, 2) == -4
    assert simple_calculator("subtract", 0, 0) == 0

def test_multiplication():
    assert simple_calculator("multiply", 5, 3) == 15
    assert simple_calculator("multiply", -2, 2) == -4
    assert simple_calculator("multiply", 0, 0) == 0

def test_division():
    assert simple_calculator("divide", 6, 3) == 2
    assert simple_calculator("divide", -6, 2) == -3
    assert simple_calculator("divide", 0, 1) == 0