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
            count_1, char_1 = heapq.heappop(heap)
            count_1 = -count_1

            if not heap:
                res.append(min(2, count_1) * char_1)
                break

            count_2, char_2 = heapq.heappop(heap)
            count_2 = -count_2

            if count_1 - count_2 > 2:
                res.append(2 * char_1)
                count_1 -= 2
            else:
                res.append(char_1)
                count_1 -= 1

            res.append(char_2)
            count_2 -= 1

            if count_1:
                heapq.heappush(heap, (-count_1, char_1))
            if count_2:
                heapq.heappush(heap, (-count_2, char_2))

        return "".join(res)
