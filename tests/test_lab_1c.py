"""
Unit tests for max_subarray_sum in labs.lab_1.lab_1c.
"""

import pytest

from labs.lab_1.lab_1c import max_subarray_sum


def test_example_from_prompt():
    # Typical mix of positives and negatives
    assert max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6  # [4, -1, 2, 1]


def test_all_negative_returns_least_negative():
    assert max_subarray_sum([-8, -3, -6, -2, -5, -4]) == -2


def test_single_element_list():
    assert max_subarray_sum([7]) == 7


def test_all_positive_accumulates_entire_list():
    assert max_subarray_sum([1, 2, 3, 4]) == 10


def test_empty_list_raises_value_error():
    with pytest.raises(ValueError, match="Input list must contain at least one number."):
        max_subarray_sum([])


def test_prefix_negative_suffix_positive():
    # Ensures algorithm resets after negative prefix
    assert max_subarray_sum([-10, 5, 6]) == 11


if __name__ == "__main__":
    pytest.main()
