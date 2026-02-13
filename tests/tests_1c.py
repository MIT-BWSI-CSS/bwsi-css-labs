import pytest
from labs.lab_1.lab_1c import max_subarray_sum

def test_empty_set():
    assert max_subarray_sum([]) == 0

def test_positive_nums_only():
    assert max_subarray_sum([1, 2, 3, 4, 5])==15 
    assert max_subarray_sum([3, 5, 1]) ==9

def test_negative_nums_only():
    assert max_subarray_sum([-1, -2])==-1


if __name__=="__main__":
    pytest.main()
