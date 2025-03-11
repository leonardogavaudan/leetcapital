from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        N = len(nums)
        expected_total = N * (1 + N) / 2
        return int(expected_total) - sum(nums)
