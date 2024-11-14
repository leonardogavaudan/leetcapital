from typing import List
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        sorted_nums = sorted(nums)
        heap = []

        i = 1
        prev = sorted_nums[0]
        count = 1
        while i < len(sorted_nums):
            if sorted_nums[i] == prev:
                count += 1
                i += 1
                continue

            if not heap or len(heap) < k:
                heapq.heappush(heap, (count, prev))
            elif heap and heap[0][0] < count:
                heapq.heappop(heap)
                heapq.heappush(heap, (count, prev))

            count = 1
            prev = sorted_nums[i]
            i += 1

        if len(heap) < k:
            heapq.heappush(heap, (count, prev))
        elif heap and heap[0][0] < count:
            heapq.heappop(heap)
            heapq.heappush(heap, (count, prev))

        res = []
        while heap:
            res.append(heapq.heappop(heap)[1])

        return res
