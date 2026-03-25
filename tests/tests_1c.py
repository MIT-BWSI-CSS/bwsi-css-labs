"""
tests_1c.py

Unit tests for max_subarray_sum in lab_1c.py.
"""

import pytest
from labs.lab_1.lab_1c import max_subarray_sum


def test_typical_case():
    assert max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6


def test_single_element_positive():
    assert max_subarray_sum([5]) == 5


def test_single_element_negative():
    assert max_subarray_sum([-7]) == -7


def test_all_positive():
    assert max_subarray_sum([1, 2, 3, 4]) == 10


def test_all_negative():
    assert max_subarray_sum([-8, -3, -6, -2, -5, -4]) == -2


def test_contains_zero():
    assert max_subarray_sum([0, -1, 0, 2, 3]) == 5


def test_empty_list():
    with pytest.raises(ValueError, match="Input list cannot be empty."):
        max_subarray_sum([])