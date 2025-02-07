from itertools import islice
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = min_ending_here = max_ending_here = nums[0]

        for num in islice(nums, 1, None):
            temp_max = max(num, num * max_ending_here, num * min_ending_here)
            temp_min = min(num, num * max_ending_here, num * min_ending_here)
            max_ending_here, min_ending_here = temp_max, temp_min
            res = max(res, max_ending_here)

        return res
