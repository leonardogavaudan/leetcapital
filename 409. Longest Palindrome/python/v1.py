from typing import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_to_count = Counter(s)
        res = 0

        for char, count in list(char_to_count.items()):
            if count > 1:
                res += (count // 2) * 2
                char_to_count[char] = count % 2
                if char_to_count[char] == 0:
                    del char_to_count[char]

        return res + min(1, len(char_to_count))
