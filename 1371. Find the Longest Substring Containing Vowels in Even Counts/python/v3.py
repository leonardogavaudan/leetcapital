class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        state = 0
        state_to_index = {0: -1}
        shift = {"a": 0, "e": 1, "i": 2, "o": 3, "u": 4}
        res = 0

        for i, c in enumerate(s):
            if c in shift:
                state ^= 1 << shift[c]

            if state in state_to_index:
                res = max(res, i - state_to_index[state])
            else:
                state_to_index[state] = i

        return res
