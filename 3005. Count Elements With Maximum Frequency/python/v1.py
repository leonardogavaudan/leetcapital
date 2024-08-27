from typing import List


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        max_freq = 0
        num_to_freq = {}
        res = 0

        for num in nums:
            if num not in num_to_freq:
                num_to_freq[num] = 0

            num_to_freq[num] += 1

            if num_to_freq[num] == max_freq:
                res += max_freq

            if num_to_freq[num] > max_freq:
                res = num_to_freq[num]
                max_freq = num_to_freq[num]

        return res
