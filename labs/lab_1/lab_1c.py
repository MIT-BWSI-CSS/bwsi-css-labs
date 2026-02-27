"""
lab_1c.py

Given a list of numbers, return the maximum sum of any contiguous subarray of the list.

Do not assume anything. Account for all edge cases.

Derived from LeetCode problem: https://leetcode.com/problems/maximum-subarray/ (leetcode medium)
"""

# TODO: Find and resolve the bug in the following implementation. Create unit tests to verify your fix.
def max_subarray_sum(nums: list[int]) -> int:
    """
    Function that takes in a list of integers and returns the maximum sum of any contiguous subarray.

    Args:
        nums (list[int]): List of integers.

    Returns:
        int: The maximum sum of any contiguous subarray.
    """

    max_current = max_global = nums[0]
    
    for num in nums:
        max_current = max(num, max_current + num)
        if max_current > max_global:
            max_global = max_current
            
    return max_global

def unit_tests():
    try: 
        assert max_subarray_sum([-2,1,-3,4,-1,2,1,-5,4])
        assert max_subarray_sum([1])
        assert max_subarray_sum([5,4,-1,7,8])
        assert max_subarray_sum([6, 7, -6, 7, 6])
        return "\n*********ALL TESTS PASSED!!*********\n"
    except AssertionError:
        return "\n*********SOMETHING FAILED!!*********\n"

# Example usage:
def main():
    print(unit_tests())

if __name__ == "__main__":
    main()