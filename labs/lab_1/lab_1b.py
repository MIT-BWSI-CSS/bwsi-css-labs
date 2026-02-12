"""
lab_1b.py

This is a script that implements a simple calculator. It takes two numbers and an operation,
then performs the operation and returns the result. 

The script asks the user to input the numbers and the operation to be performed,
and prints the result to the terminal window.

"""
def simple_calculator(operation: str, num1, num2) -> float:
    try:
        num1 = float(num1)
        num2 = float(num2)
    except (ValueError, TypeError):
        raise ValueError("That's not a number")

    if operation == "add":
        return num1 + num2

    elif operation == "subtract":
        return num1 - num2

    elif operation == "multiply":
        return num1 * num2

    elif operation == "divide":
        if num2 == 0:
            raise ValueError("Cannot divide by zero.")
        return num1 / num2

    else:
        raise ValueError(
            "Invalid operation. Please choose from 'add', 'subtract', 'multiply', or 'divide'."
        )


def main():
    print("===== Simple Calculator =====")

    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()

    try:
        result = simple_calculator(operation, num1, num2)
        print(f"The result is: {result}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
