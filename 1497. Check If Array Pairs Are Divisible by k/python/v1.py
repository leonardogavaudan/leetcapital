from typing import List


class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        count = {}

        for num in arr:
            target = (k - num % k) % k
            if target in count:
                count[target] -= 1
                if count[target] == 0:
                    del count[target]
            else:
                if num % k not in count:
                    count[num % k] = 0
                count[num % k] += 1

        return len(count) == 0
