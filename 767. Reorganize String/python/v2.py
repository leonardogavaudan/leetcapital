from collections import Counter
import heapq


class Solution:
    def reorganizeString(self, s: str) -> str:
        res = []
        counter = Counter(s)
        heap = []
        for char, count in counter.items():
            if count > len(s) // 2 + len(s) % 2 != 0:
                return ""
            heapq.heappush(heap, (-count, char))

        while heap:
            first_count, first_char = heapq.heappop(heap)
            first_count *= -1
            first_count -= 1
            res.append(first_char)

            if not heap:
                break

            second_count, second_char = heapq.heappop(heap)
            second_count *= -1
            second_count -= 1
            res.append(second_char)

            if first_count > 0:
                heapq.heappush(heap, (-first_count, first_char))
            if second_count > 0:
                heapq.heappush(heap, (-second_count, second_char))

        return "".join(res)
