from collections import Counter
from typing import List
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        heap = []

        for num, count in counter.items():
            if len(heap) < k:
                heapq.heappush(heap, (count, num))
            elif heap[0][0] < count:
                heapq.heappop(heap)
                heapq.heappush(heap, (count, num))

        return list(map(lambda x: x[1], heap))
