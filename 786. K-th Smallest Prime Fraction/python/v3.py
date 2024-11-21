from typing import List
import heapq


class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        heap = []

        for i, num in enumerate(arr[slice(0, -1)]):
            heapq.heappush(heap, (num / arr[-1], i, len(arr) - 1))

        for _ in range(k - 1):
            _, start, end = heapq.heappop(heap)
            if start < end - 1:
                end -= 1
                heapq.heappush(heap, (arr[start] / arr[end], start, end))

        _, start, end = heapq.heappop(heap)

        return [arr[start], arr[end]]
