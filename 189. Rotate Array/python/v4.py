from math import gcd
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        for i in range(gcd(k, len(nums))):
            index = i
            temp = nums[index]
            while True:
                next_index = (index + k) % len(nums)
                nums[next_index], temp = temp, nums[next_index]
                if next_index == i:
                    break
                index = next_index
