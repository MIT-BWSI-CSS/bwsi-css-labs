def simple_calculator(operation: str, num1: float, num2: float) -> float:
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

def sanitize_input(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    print("===== Simple Calculator =====")
    num1 = sanitize_input("Enter the first number: ")
    num2 = sanitize_input("Enter the second number: ")
    operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()

    try:
        result = simple_calculator(operation, num1, num2)
        print(f"The result of {operation}ing {num1} and {num2} is: {result}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()