from typing import List


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        res = len(nums)
        total = sum(nums)
        if total % p == 0:
            return 0

        remainder = total % p
        prefix_sum = 0
        prefix_sum_to_latest_index = {0: -1}

        for i, num in enumerate(nums):
            prefix_sum = (prefix_sum + num) % p
            prefix_sum_target = (prefix_sum - remainder + p) % p
            if prefix_sum_target in prefix_sum_to_latest_index:
                res = min(res, i - prefix_sum_to_latest_index[prefix_sum_target])
            prefix_sum_to_latest_index[prefix_sum] = i

        return res if res < len(nums) else -1
