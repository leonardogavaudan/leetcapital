import heapq
from typing import List


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        heap = [(x[0], 0, i) for i, x in enumerate(nums)]
        max_value = max((x[0] for x in nums))
        heapq.heapify(heap)
        best_max_value = max_value
        best_min_value = heap[0][0]

        while heap:
            min_value, col, row = heapq.heappop(heap)

            if max_value - min_value < best_max_value - best_min_value:
                best_min_value, best_max_value = min_value, max_value

            if col == len(nums[row]) - 1:
                return [best_min_value, best_max_value]

            next_val = nums[row][col + 1]
            max_value = max(max_value, next_val)
            heapq.heappush(heap, (next_val, col + 1, row))

        raise AssertionError("unreachable branch")
