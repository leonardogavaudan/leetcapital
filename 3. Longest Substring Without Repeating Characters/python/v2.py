class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        char_seen_to_last_seen = {}
        str_start = 0

        for str_end, c in enumerate(s):
            if c in char_seen_to_last_seen and char_seen_to_last_seen[c] >= str_start:
                str_start = char_seen_to_last_seen[c] + 1
            char_seen_to_last_seen[c] = str_end

            res = max(res, str_end - str_start + 1)

        return res
