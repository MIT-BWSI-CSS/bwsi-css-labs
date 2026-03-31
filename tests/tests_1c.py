"""
tests_1c.py

This module contains unit tests for the max_subarray_sum function defined in lab_1c.py.
"""

import pytest
from labs.lab_1.lab_1c import max_subarray_sum

def test_single_element():
    assert max_subarray_sum([1]) == 1                      # Test for single element

def test_all_positive():
    assert max_subarray_sum([1, 2, 3, 4]) == 10           # Test for all positive numbers

def test_all_negative():
    assert max_subarray_sum([-1, -2, -3, -4]) == -1      # Test for all negative numbers

def test_mixed_numbers():
    assert max_subarray_sum([-2, -3, 4, -1, -2, 1, 5, -3]) == 7  # Test for mixed numbers

def test_all_same():
    assert max_subarray_sum([2, 2, 2, 2]) == 8            # Test for all same positive numbers
    assert max_subarray_sum([-2, -2, -2, -2]) == -2      # Test for all same negative numbers

def test_empty_list():                       # Test if raises specified error
    assert max_subarray_sum([]) == 0                                # Line of code to be tested

def test_correct_datatype():
    assert max_subarray_sum("String") == 0 and max_subarray_sum(["String", "String"]) == 0

if __name__ == "__main__":
    pytest.main()