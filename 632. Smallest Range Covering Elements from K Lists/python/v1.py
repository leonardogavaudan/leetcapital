from typing import List
import heapq


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        heap = []
        current_max = float("-inf")

        for i, row in enumerate(nums):
            if row:
                heapq.heappush(heap, (row[0], i, 0))
                current_max = max(current_max, row[0])

        best_range = [heap[0][0], current_max]

        while len(heap) == len(nums):
            val, list_idx, pos = heapq.heappop(heap)

            if current_max - val < best_range[1] - best_range[0]:
                best_range = [val, current_max]

            if pos + 1 < len(nums[list_idx]):
                next_val = nums[list_idx][pos + 1]
                heapq.heappush(heap, (next_val, list_idx, pos + 1))
                current_max = max(current_max, next_val)

        return best_range
