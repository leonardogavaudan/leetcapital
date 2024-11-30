from collections import Counter
import heapq


class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        if max(counter.values()) > (len(s) + 1) // 2:
            return ""

        heap = []
        for char, value in counter.items():
            heapq.heappush(heap, (-value, char))

        res = []
        while heap:
            count_1, char_1 = heapq.heappop(heap)
            count_1 = -count_1 - 1
            res.append(char_1)

            if not heap:
                break

            count_2, char_2 = heapq.heappop(heap)
            count_2 = -count_2 - 1
            res.append(char_2)

            if count_1:
                heapq.heappush(heap, (-count_1, char_1))
            if count_2:
                heapq.heappush(heap, (-count_2, char_2))

        return "".join(res)
