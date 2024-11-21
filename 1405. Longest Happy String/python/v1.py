import heapq


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = []
        heap = []

        if a:
            heapq.heappush(heap, (-a, "a"))
        if b:
            heapq.heappush(heap, (-b, "b"))
        if c:
            heapq.heappush(heap, (-c, "c"))

        while heap:
            count_1, char1 = heapq.heappop(heap)
            count_1 = -count_1
            res.append(char1 * min(count_1, 2))
            count_1 -= min(count_1, 2)
            if not heap:
                break

            count_2, char2 = heapq.heappop(heap)
            count_2 = -count_2
            count_2_to_add = min(1 if count_1 - count_2 > 0 else 2, count_2)
            res.append(char2 * count_2_to_add)
            count_2 -= count_2_to_add

            if count_1:
                heapq.heappush(heap, (-count_1, char1))
            if count_2:
                heapq.heappush(heap, (-count_2, char2))

        return "".join(res)
