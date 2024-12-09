from collections import defaultdict
from typing import List


class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        mod_to_count = defaultdict(int)
        for num in arr:
            mod_to_count[num % k] += 1
        for mod, count in mod_to_count.items():
            target = (k - mod) % k
            if target == mod and count % 2 == 1:
                return False
            elif count != mod_to_count[target]:
                return False
        return True
