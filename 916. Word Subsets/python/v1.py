from collections import Counter, defaultdict
from typing import List


class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        res = []

        hash_map_universal = defaultdict(int)

        for word in words2:
            count = Counter(word)
            for key, value in count.items():
                hash_map_universal[key] = max(hash_map_universal[key], value)

        for word in words1:
            count = Counter(word)
            if all(
                (
                    key in count and value <= count[key]
                    for key, value in hash_map_universal.items()
                )
            ):
                res.append(word)

        return res
