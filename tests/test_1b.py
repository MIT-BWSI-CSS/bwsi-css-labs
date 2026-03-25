"""
tests_1b.py

This module contains unit tests for the simple_calculator function defined in lab_1b.py.
The tests cover various scenarios for addition, subtraction, multiplication, and division operations
including edge cases such as division by zero and invalid operations. The tests are implemented using the pytest framework. Dummy comment to make commit
"""

import pytest
from labs.lab_1.lab_1b import simple_calculator

def test_addition():
    assert simple_calculator("add", 5, 3) == 8          # Test for positive numbers
    assert simple_calculator("add", -2, 2) == 0         # Test for negative and positive number
    assert simple_calculator("add", 0, 0) == 0          # Test for zero addition

def test_subtraction():
    assert simple_calculator("subtract", 5, 3) == 2     # Test for positive numbers
    assert simple_calculator("subtract", -2, -2) == 0   # Test for negative numbers
    assert simple_calculator("subtract", 0, 5) == -5    # Test for zero minuend

def test_multiplication():
    assert simple_calculator("multiply", 5, 3) == 15    # Test for positive numbers
    assert simple_calculator("multiply", -2, 2) == -4   # Test for negative and positive number
    assert simple_calculator("multiply", 0, 100) == 0   # Test for multiplication by zero

def test_division():
    assert simple_calculator("divide", 6, 3) == 2       # Test for positive numbers
    assert simple_calculator("divide", -4, 2) == -2     # Test for negative and positive number
    assert simple_calculator("divide", 5, 2) == 2.5     # Test for division resulting in float

def test_division_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero."):
        simple_calculator("divide", 5, 0)               # Test division by zero

def test_invalid_operation():
    with pytest.raises(ValueError, match="Invalid operation. Please choose from 'add', 'subtract', 'multiply', or 'divide'."):
        simple_calculator("modulus", 5, 3)              # Test for invalid operation
    with pytest.raises(ValueError, match="Invalid operation. Please choose from 'add', 'subtract', 'multiply', or 'divide'."):
        simple_calculator("", 5, 3)                     # Test for empty operation

def test_operation_case_insensitivity():
    assert simple_calculator("ADD", 5, 3) == 8         # Test for uppercase operation
    assert simple_calculator("Subtract", 5, 3) == 2    # Test for mixed case operation        
    assert simple_calculator("MULTIPLY", 5, 3) == 15   # Test for uppercase operation
    assert simple_calculator("DIVIDE", 6, 3) == 2      # Test for uppercase operation

def test_operation_with_whitespace():
    assert simple_calculator(" add ", 5, 3) == 8       # Test for operation with leading and trailing whitespace
    assert simple_calculator(" subtract ", 5, 3) == 2  # Test for operation with leading and trailing whitespace
    assert simple_calculator(" multiply ", 5, 3) == 15 # Test for operation with leading and trailing whitespace
    assert simple_calculator(" divide ", 6, 3) == 2    # Test for operation with leading and trailing whitespace

def test_operation_with_non_numeric_input():
    with pytest.raises(ValueError):
        simple_calculator("add", "five", 3)             # Test for  non-numeric input for num1
    with pytest.raises(ValueError):
        simple_calculator("subtract", 5, "three")       # Test for non-numeric input for num2        

if __name__ == "__main__":
    pytest.main()