class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_to_count = {}
        for c in s:
            if c not in char_to_count:
                char_to_count[c] = 0
            char_to_count[c] += 1

        for index, c in enumerate(s):
            if char_to_count[c] == 1:
                return index

        return -1
