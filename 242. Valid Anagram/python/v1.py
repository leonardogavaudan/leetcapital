class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_char_to_count = {}

        for c in s:
            s_char_to_count[c] = s_char_to_count.get(c, 0) + 1

        for c in t:
            if c not in s_char_to_count:
                return False
            s_char_to_count[c] -= 1
            if s_char_to_count[c] == 0:
                del s_char_to_count[c]

        return len(s_char_to_count) == 0
