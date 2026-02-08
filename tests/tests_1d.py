"""
tests_1c.py

This module contains unit tests for the simple_calculator function defined in lab_1b.py.
"""

import pytest
from labs.lab_1.lab_1c import max_subarray_sum

def test_max():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]               # Test for empty operation

if __name__ == "__main__":
    pytest.main()