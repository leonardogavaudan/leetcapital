from typing import List


class Solution:
    def validSubarraySize(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        nums.append(0)
        stack = []
        for i in range(n + 1):
            while stack and nums[stack[-1]] >= nums[i]:
                idx = stack.pop()
                height = nums[idx]
                width = i - stack[-1] - 1 if stack else i
                if height > threshold / width:
                    return width
            stack.append(i)
        return -1
