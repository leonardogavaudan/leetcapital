from typing import Counter


class Solution:
    def minimumPushes(self, word: str) -> int:
        res = 0
        distinct_char_count = 0
        char_to_count = Counter(word)
        char_counts = list(char_to_count.values())
        char_counts.sort(reverse=True)

        for count in char_counts:
            distinct_char_count += 1
            res += count * ((distinct_char_count // 8) + (distinct_char_count % 8 != 0))

        return res
