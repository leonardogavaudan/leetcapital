import heapq
from typing import List


class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        res = 0
        heap = [(num, i) for i, num in enumerate(nums)]
        heapq.heapify(heap)

        for i in range(1, right + 1):
            num, num_i = heapq.heappop(heap)

            if i >= left:
                res += num

            if num_i + 1 < n:
                heapq.heappush(heap, (num + nums[num_i + 1], num_i + 1))

        return res % (10**9 + 7)
