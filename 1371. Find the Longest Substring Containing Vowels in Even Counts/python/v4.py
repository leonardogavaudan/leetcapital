class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        res = 0
        bitmask = 0
        first_seen = [-1] * 32
        first_seen[0] = 0
        shift = {
            "a": 0,
            "e": 1,
            "i": 2,
            "o": 3,
            "u": 4,
        }

        for i, c in enumerate(s, 1):
            if c in shift:
                bitmask ^= 1 << shift[c]

            if first_seen[bitmask] == -1:
                first_seen[bitmask] = i
            else:
                res = max(res, i - first_seen[bitmask])

        return res
