"""
tests_1c.py

This module contains unit tests for the simple_calculator function defined in lab_1b.py.
"""

import pytest
from labs.lab_1.lab_1b import simple_calculator
from labs.lab_1.lab_1c import max_subarray_sum

def test_max():
    assert max_subarray_sum([-2,1,-3,4,-1,2,1,-5,4]) == 6                # Test for empty operation

if __name__ == "__main__":
    pytest.main()