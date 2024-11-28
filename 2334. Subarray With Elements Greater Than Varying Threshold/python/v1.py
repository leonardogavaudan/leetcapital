from typing import List


class Solution:
    def validSubarraySize(self, nums: List[int], threshold: int) -> int:
        nums = [0] + nums + [0]
        stack = [0]

        for i in range(1, len(nums)):
            while nums[stack[-1]] > nums[i]:
                height = nums[stack.pop()]
                width = i - 1 - stack[-1]
                if width > 0 and height > threshold / width:
                    return width
            stack.append(i)

        return -1
