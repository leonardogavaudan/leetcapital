import heapq


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        for char, count in [("a", a), ("b", b), ("c", c)]:
            if count > 0:
                heap.append((-count, char))
        heapq.heapify(heap)

        res = []
        while heap:
            count, char = heapq.heappop(heap)
            if len(res) >= 2 and char == res[-1] == res[-2]:
                if not heap:
                    break

                second_count, second_char = heapq.heappop(heap)
                res.append(second_char)
                if second_count < -1:
                    heapq.heappush(heap, (second_count + 1, second_char))
                heapq.heappush(heap, (count, char))
            else:
                res.append(char)
                if count < -1:
                    heapq.heappush(heap, (count + 1, char))

        return "".join(res)
