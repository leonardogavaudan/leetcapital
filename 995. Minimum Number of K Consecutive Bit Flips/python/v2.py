from typing import List


class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        res = 0
        is_flip = 0
        for i in range(len(nums)):
            if i - k >= 0 and nums[i - k] == 2:
                is_flip ^= 1

            total = is_flip + nums[i]
            if total % 2 == 0:
                if i + k - 1 >= len(nums):
                    return -1

                res += 1
                nums[i] = 2
                is_flip ^= 1

        return res
