"""
tests_1d.py

This module contains unit tests for the two_sum in lab_1d.py
"""

import pytest
from labs.lab_1.lab_1d import two_sum

def test_two_sum():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]
    assert two_sum([3, 3], 6) == [0, 1]
    assert two_sum([1, 2, 3, 4, 5], 9) == [3, 4]
    assert two_sum([1, 2, 3, 4, 5], 3) == [0,1]
    assert two_sum([1, 2, 3, 4, 5], 10) == []

if __name__ == "__main__":
    pytest.main()
