from typing import List
import heapq


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        heap = [(l[0], 0, l_i) for l_i, l in enumerate(nums)]
        heapq.heapify(heap)
        best_min = heap[0][0]
        best_max = max(map(lambda x: x[0], heap))
        curr_max = best_max

        while heap:
            _, index, list_index = heapq.heappop(heap)
            if index == len(nums[list_index]) - 1:
                return [best_min, best_max]

            next_val = nums[list_index][index + 1]
            curr_max = max(curr_max, next_val)
            heapq.heappush(heap, (next_val, index + 1, list_index))

            if curr_max - heap[0][0] < best_max - best_min:
                best_min, best_max = heap[0][0], curr_max

        raise IndexError("Heap not supposed to get to empty state")
