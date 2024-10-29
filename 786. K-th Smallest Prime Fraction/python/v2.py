import heapq
from typing import List


class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        heap = []
        for i in range(0, len(arr) - 1):
            heapq.heappush(heap, (arr[i] / arr[-1], i, len(arr) - 1))

        for _ in range(k - 1):
            _, start, end = heapq.heappop(heap)

            end -= 1
            if start < end:
                heapq.heappush(heap, (arr[start] / arr[end], start, end))

        _, start, end = heapq.heappop(heap)

        return [arr[start], arr[end]]
