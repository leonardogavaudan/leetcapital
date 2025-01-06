from typing import List


class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        flip_count = 0
        is_flipped = 0

        for i in range(len(nums)):
            if i - k >= 0 and nums[i - k] == -1:
                is_flipped ^= 1

            if (nums[i] + is_flipped) % 2 == 0:
                if i > len(nums) - k:
                    return -1

                nums[i] = -1
                flip_count += 1
                is_flipped ^= 1

        return flip_count
