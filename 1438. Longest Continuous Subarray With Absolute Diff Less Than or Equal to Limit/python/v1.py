from collections import deque
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        res = 0
        max_queue = deque([])
        min_queue = deque([])
        left = 0

        for right in range(len(nums)):
            while max_queue and nums[right] > max_queue[-1]:
                max_queue.pop()
            max_queue.append(nums[right])

            while min_queue and nums[right] < min_queue[-1]:
                min_queue.pop()
            min_queue.append(nums[right])

            while max_queue[0] - min_queue[0] > limit:
                if max_queue[0] == nums[left]:
                    max_queue.popleft()
                if min_queue[0] == nums[left]:
                    min_queue.popleft()
                left += 1

            res = max(res, right - left + 1)

        return res
