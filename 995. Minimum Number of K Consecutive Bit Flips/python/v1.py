from typing import List


class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        res = 0
        current_flips = 0

        for i in range(len(nums)):
            if i >= k and nums[i - k] == 2:
                current_flips -= 1

            if (nums[i] + current_flips) % 2 == 0:
                if i + k - 1 >= len(nums):
                    return -1
                res += 1
                current_flips += 1
                nums[i] = 2

        return res
