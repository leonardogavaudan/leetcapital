from typing import List


class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        res = 0
        current_flips = 0
        n = len(nums)

        for i in range(n):
            if i >= k and nums[i - k] == 2:
                current_flips -= 1

            if (nums[i] + current_flips) % 2 == 0:
                if i + k > n:
                    return -1
                res += 1
                current_flips += 1
                nums[i] = 2

        return res
