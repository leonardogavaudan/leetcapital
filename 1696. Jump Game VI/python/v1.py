from collections import deque
from typing import List


class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        dp = [float("-inf")] * len(nums)
        dp[0] = nums[0]

        monotonic_queue = deque([nums[0]])

        for i in range(1, len(nums)):
            dp[i] = nums[i] + monotonic_queue[0]

            while monotonic_queue and monotonic_queue[-1] < dp[i]:
                monotonic_queue.pop()
            monotonic_queue.append(int(dp[i]))

            index_to_be_removed = i - k
            if (
                index_to_be_removed >= 0
                and monotonic_queue[0] == dp[index_to_be_removed]
            ):
                monotonic_queue.popleft()

        return int(dp[-1])
