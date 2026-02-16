"""
test_1c.py

This module contains unit tests for the maximum subarray sum function defined in lab_1c.py.
"""

import pytest
from labs.lab_1.lab_1c import max_subarray_sum

def test_example():
    assert max_subarray_sum([-2,1,-3,4,-1,2,1,-5,4]) == 6 # test given example

def test_single_positive():
    assert max_subarray_sum([3]) == 3 # test a single positive number

def test_single_negative():
    assert max_subarray_sum([-5]) == -5 # test a single negative number

def test_all_positive():
    assert max_subarray_sum([1, 5, 7, 2]) == 15 # test a list of all positives

def test_all_negative():
    assert max_subarray_sum([-3, -2, -7]) == -2 # test a list of all negatives

def test_with_zero():
    assert max_subarray_sum([-2, -5, 0]) == 0 # test a zero in the list

def test_all_zeroes():
    assert max_subarray_sum([0, 0, 0]) == 0 # test a list of all zeroes

if __name__ == "__main__":
    pytest.main()