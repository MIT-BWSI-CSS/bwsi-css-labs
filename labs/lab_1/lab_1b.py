"""
lab_1b.py

This is a script that implements a simple calculator. It takes two numbers and an operation,
then performs the operation and returns the result. 

The script asks the user to input the numbers and the operation to be performed,
and prints the result to the terminal window.

"""
def get_operation(prompt : str) -> str:
    valid_operations = ["add","subtract", "multiply", "divide"]
    while True:
        operation = input(prompt).strip().lower()
        if operation in valid_operations:
            return operation
        else: 
            print("Please enter add, subtract, multiply, or divide")

def get_number(prompt:str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a nummerical value")

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

    # Ask the user for sample input    
    num1 = get_number("Enter the first number: ")
    num2 = get_number("Enter the second number: ")
    operation = get_operation("Enter the operation (add, subtract, multiply, divide): ")
    try:
        result = simple_calculator(operation, num1, num2)
        print(f"The result of {operation}ing {num1} and {num2} is: {result}")
    except ValueError as A:
        print(A)
        


if __name__ == "__main__":
    main()
# Perform the calculation and display the result