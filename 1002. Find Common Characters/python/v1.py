from typing import Dict, List


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        char_to_count: Dict[str, int] = {}
        for c in words[0]:
            if c not in char_to_count:
                char_to_count[c] = 0
            char_to_count[c] += 1

        for word in words[1:]:
            new_char_to_count: Dict[str, int] = {}
            for c in word:
                if c in char_to_count:
                    if c not in new_char_to_count:
                        new_char_to_count[c] = 1
                    elif char_to_count[c] > new_char_to_count[c]:
                        new_char_to_count[c] += 1
            char_to_count = new_char_to_count

        res = []
        for char, count in char_to_count.items():
            for _ in range(count):
                res.append(char)

        return res
