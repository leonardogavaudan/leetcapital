from collections import Counter


class Solution:
    def minimumPushes(self, word: str) -> int:
        res = 0
        index = 0
        keys = [1] * 8
        counter = Counter(word)
        for _, count in counter.most_common():
            res += keys[index] * count
            keys[index] += 1
            index = (index + 1) % 8

        return res
