from collections import deque
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        res = 0
        decreasing_queue = deque([])
        increasing_queue = deque([])
        left = 0

        for right in range(len(nums)):
            while increasing_queue and increasing_queue[-1] > nums[right]:
                increasing_queue.pop()
            increasing_queue.append(nums[right])

            while decreasing_queue and decreasing_queue[-1] < nums[right]:
                decreasing_queue.pop()
            decreasing_queue.append(nums[right])

            while decreasing_queue[0] - increasing_queue[0] > limit:
                if decreasing_queue[0] == nums[left]:
                    decreasing_queue.popleft()
                if increasing_queue[0] == nums[left]:
                    increasing_queue.popleft()
                left += 1

            res = max(res, right - left + 1)

        return res
