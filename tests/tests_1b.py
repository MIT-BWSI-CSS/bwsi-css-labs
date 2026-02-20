"""
tests_1b.py

This module contains unit tests for the simple_calculator function defined in lab_1b.py.
"""

import pytest
from labs.lab_1.lab_1b import simple_calculator

def test_invalid_operation():
    with pytest.raises(ValueError, match="Invalid operation. Please choose from 'add', 'subtract', 'multiply', or 'divide'."):
        simple_calculator("modulus", 5, 3)
    with pytest.raises(ValueError, match="Invalid operation. Please choose from 'add', 'subtract', 'multiply', or 'divide'."):
        simple_calculator("", 5, 3)

def test_addition():
    assert simple_calculator("add", 5, 3) == 8          # Test for positive numbers
    assert simple_calculator("add", -2, 2) == 0         # Test for negative and positive number
    assert simple_calculator("add", 0, 0) == 0          # Test for zero addition
    assert simple_calculator("add", 1, 1) == 2
    assert simple_calculator("add", 4, 4) == 8

def test_subtraction():
    assert simple_calculator("subtract", 5, 3) == 2     # Test for positive numbers
    assert simple_calculator("subtract", -2, -2) == 0   # Test for negative numbers
    assert simple_calculator("subtract", 0, 5) == -5    # Test for zero minuend
    assert simple_calculator("subtract", 9, 4) == 5

def test_multiplication():
    assert simple_calculator("multiply", 5, 3) == 15    # Test for positive numbers
    assert simple_calculator("multiply", -2, 2) == -4   # Test for negative and positive number
    assert simple_calculator("multiply", 0, 100) == 0   # Test for multiplication by zero
    assert simple_calculator("multiply", 5, 5) == 25

def test_division():
    assert simple_calculator("divide", 6, 3) == 2       # Test for positive numbers
    assert simple_calculator("divide", -4, 2) == -2     # Test for negative and positive number
    assert simple_calculator("divide", 5, 2) == 2.5     # Test for division resulting in float
    assert simple_calculator("divide", 9, 3) == 3

def test_division_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero."):
        simple_calculator("divide", 5, 0)               # Test division by zero
        simple_calculator("divide", 4, 0)

def test_invalid_operation():
    with pytest.raises(ValueError, match="Invalid operation. Please choose from 'add', 'subtract', 'multiply', or 'divide'."):
        simple_calculator("modulus", 5, 3)              # Test for invalid operation
    with pytest.raises(ValueError, match="Invalid operation. Please choose from 'add', 'subtract', 'multiply', or 'divide'."):
        simple_calculator("", 5, 3)                     # Test for empty operation

if __name__ == "__main__":
    pytest.main()
