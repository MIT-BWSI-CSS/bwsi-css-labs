import pytest
from labs.lab_1.lab_1c import max_subarray_sum

def testSolution():
    assert max_subarray_sum([-2,1,-3,4,-1,2,1,-5,4]) == 6
    assert max_subarray_sum([1]) == 1
    assert max_subarray_sum([5,4,-1,7,8]) == 23
