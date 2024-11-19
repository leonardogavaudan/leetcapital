class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        state = 0
        state_to_first_seen = {0: -1}
        char_to_shift = {
            "a": 0,
            "e": 1,
            "i": 2,
            "o": 3,
            "u": 4,
        }
        res = 0

        for i, char in enumerate(s):
            if char in char_to_shift:
                state ^= 1 << char_to_shift[char]

            if state in state_to_first_seen:
                res = max(res, i - state_to_first_seen[state])
            else:
                state_to_first_seen[state] = i

        return res
