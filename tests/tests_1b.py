"""
tests_1b.py

This module contains unit tests for the simple_calculator function defined in lab_1b.py.
"""

import pytest
from labs.lab_1.lab_1b import simple_calculator


def test_addition():
    assert simple_calculator("add", 5, 3) == 8  # Test for positive numbers
    assert simple_calculator("add", -2, 2) == 0  # Test for negative and positive number
    assert simple_calculator("add", 0, 0) == 0  # Test for zero addition


def test_subtraction():
    assert simple_calculator("subtract", 5, 3) == 2  # Test for positive numbers
    assert simple_calculator("subtract", -2, -2) == 0  # Test for negative numbers
    assert simple_calculator("subtract", 0, 5) == -5  # Test for zero minuend


def test_multiplication():
    assert simple_calculator("multiply", 5, 3) == 15  # Test for positive numbers
    assert (
        simple_calculator("multiply", -2, 2) == -4
    )  # Test for negative and positive number
    assert simple_calculator("multiply", 0, 100) == 0  # Test for multiplication by zero


def test_division():
    assert simple_calculator("divide", 6, 3) == 2  # Test for positive numbers
    assert (
        simple_calculator("divide", -4, 2) == -2
    )  # Test for negative and positive number
    assert (
        simple_calculator("divide", 5, 2) == 2.5
    )  # Test for division resulting in float


def test_float_operation():
    assert (
        abs(simple_calculator("subtract", 3.3, 3.2) - 0.1) < 1e-6
    )  # Test for operations on floats


def test_division_by_zero():
    with pytest.raises(ValueError):
        simple_calculator("divide", 5, 0)  # Test division by zero


def test_invalid_operation():
    with pytest.raises(ValueError):
        simple_calculator("modulus", 5, 3)  # Test for invalid operation
    with pytest.raises(ValueError):
        simple_calculator("", 5, 3)  # Test for empty operation


if __name__ == "__main__":
    pytest.main()
