from typing import List


class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        hash_map = {}
        for num in arr:
            target = (k - (num % k)) % k
            if target in hash_map:
                hash_map[target] -= 1
                if hash_map[target] == 0:
                    del hash_map[target]
            else:
                if num % k not in hash_map:
                    hash_map[num % k] = 0
                hash_map[num % k] += 1

        return len(hash_map) == 0
