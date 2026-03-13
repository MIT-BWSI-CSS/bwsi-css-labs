import unittest

def max_subarray_sum(nums: list[int]) -> int:
    if not nums:
        raise ValueError("nums must not be empty")

    max_current = max_global = nums[0]

    for num in nums[1:]:
        max_current = max(num, max_current + num)
        if max_current > max_global:
            max_global = max_current

    return max_global


class TestMaxSubarraySum(unittest.TestCase):
    def test_example_case(self):
        self.assertEqual(max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)

    def test_single_positive(self):
        self.assertEqual(max_subarray_sum([5]), 5)

    def test_single_negative(self):
        self.assertEqual(max_subarray_sum([-5]), -5)

    def test_all_negative(self):
        self.assertEqual(max_subarray_sum([-8, -3, -6, -2, -5, -4]), -2)

    def test_all_positive(self):
        self.assertEqual(max_subarray_sum([1, 2, 3, 4]), 10)

    def test_mixed_values(self):
        self.assertEqual(max_subarray_sum([5, -2, 3, 4]), 10)

    def test_contains_zeroes(self):
        self.assertEqual(max_subarray_sum([0, 0, 0]), 0)

    def test_empty_list_raises(self):
        with self.assertRaises(ValueError):
            max_subarray_sum([])


if __name__ == "__main__":
    unittest.main()