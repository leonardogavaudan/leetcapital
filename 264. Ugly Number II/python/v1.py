import heapq


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        seen = set()
        heap = [1]
        for _ in range(n - 1):
            current = heapq.heappop(heap)
            for x in [2, 3, 5]:
                new = current * x
                if new not in seen:
                    heapq.heappush(heap, new)
                    seen.add(new)

        return heap[0]
