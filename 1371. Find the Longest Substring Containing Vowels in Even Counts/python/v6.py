class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        res = 0
        state = 0
        state_to_first_seen_index = {0: -1}
        char_to_shift = {
            "a": 1,
            "e": 2,
            "i": 3,
            "o": 4,
            "u": 5,
        }

        for i, c in enumerate(s):
            if c in char_to_shift:
                state = state ^ 1 << char_to_shift[c]

            if state in state_to_first_seen_index:
                length = i - state_to_first_seen_index[state]
                res = max(res, length)
            else:
                state_to_first_seen_index[state] = i

        return res
