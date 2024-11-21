from typing import List
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        heap = []
        count = 1
        i = 1
        while i <= len(nums):
            while i < len(nums) and nums[i - 1] == nums[i]:
                count += 1
                i += 1

            if len(heap) == k:
                if count > heap[0][0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (count, nums[i - 1]))
            else:
                heapq.heappush(heap, (count, nums[i - 1]))

            count = 1
            i += 1

        return [element[1] for element in heap]
