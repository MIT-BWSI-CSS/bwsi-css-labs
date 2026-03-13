import unittest

def two_sum(nums: list[int], target: int) -> list[int]:
    num_to_index = {}
    for index, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], index]
        num_to_index[num] = index
    return []


class TestTwoSum(unittest.TestCase):
    def test_basic_case(self):
        self.assertEqual(two_sum([2, 7, 11, 15], 9), [0, 1])

    def test_other_case(self):
        self.assertEqual(two_sum([3, 2, 4], 6), [1, 2])

    def test_duplicate_values(self):
        self.assertEqual(two_sum([3, 3], 6), [0, 1])

    def test_negative_numbers(self):
        self.assertEqual(two_sum([-1, -2, -3, -4, -5], -8), [2, 4])

    def test_no_solution_fallback(self):
        self.assertEqual(two_sum([1, 2, 3], 100), [])


if __name__ == "__main__":
    unittest.main()