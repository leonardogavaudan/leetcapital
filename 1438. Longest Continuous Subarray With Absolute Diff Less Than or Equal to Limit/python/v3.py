from collections import deque
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        res = 0
        min_queue = deque()
        max_queue = deque()
        l = 0

        for r in range(len(nums)):
            while min_queue and min_queue[-1] > nums[r]:
                min_queue.pop()
            min_queue.append(nums[r])

            while max_queue and max_queue[-1] < nums[r]:
                max_queue.pop()
            max_queue.append(nums[r])

            while max_queue[0] - min_queue[0] > limit:
                if min_queue[0] == nums[l]:
                    min_queue.popleft()
                if max_queue[0] == nums[l]:
                    max_queue.popleft()
                l += 1

            res = max(res, r - l + 1)

        return res
