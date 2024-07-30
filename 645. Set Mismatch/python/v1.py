from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        seen = set()
        double = 0
        expected_total = int(len(nums) * (len(nums) + 1) / 2)
        actual_total = 0
        for num in nums:
            if num in seen:
                double = num
            else:
                seen.add(num)
            actual_total += num
        missing = expected_total - (actual_total - double)

        return [double, missing]
