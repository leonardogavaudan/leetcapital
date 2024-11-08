from collections import Counter
import heapq


class Solution:
    def reorganizeString(self, s: str) -> str:
        res = []
        counter = Counter(s)
        heap = []

        for char, count in counter.items():
            heapq.heappush(heap, (-count, char))

        while heap:
            negative_count, char = heapq.heappop(heap)
            res.append(char)
            negative_count += 1

            if not heap:
                if negative_count < 0:
                    return ""
                else:
                    break

            next_negative_count, next_char = heapq.heappop(heap)
            res.append(next_char)
            next_negative_count += 1

            if negative_count != 0:
                heapq.heappush(heap, (negative_count, char))
            if next_negative_count != 0:
                heapq.heappush(heap, (next_negative_count, next_char))

        return "".join(res)
