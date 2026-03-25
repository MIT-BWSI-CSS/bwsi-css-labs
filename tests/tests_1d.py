"""
tests_1d.py

Unit tests for two_sum in lab_1d.py.
"""

import pytest
from labs.lab_1.lab_1d import two_sum


def test_basic_case():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]


def test_another_case():
    assert two_sum([3, 2, 4], 6) == [1, 2]


def test_with_negatives():
    assert two_sum([-1, -2, -3, -4, -5], -8) == [2, 4]


def test_same_number_used_twice():
    assert two_sum([3, 3], 6) == [0, 1]


def test_large_numbers():
    assert two_sum([1000000, 500000, 500000], 1000000) == [1, 2]