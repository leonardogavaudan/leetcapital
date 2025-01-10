class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        res = 0
        char_to_shift = {
            chr(x): x - ord("a") + 1 for x in range(ord("a"), ord("j") + 1)
        }
        state = 0
        state_seen_count = {0: 1}

        for c in word:
            if c in char_to_shift:
                state ^= 1 << char_to_shift[c]

            if state in state_seen_count:
                res += state_seen_count[state]
                state_seen_count[state] += 1
            else:
                state_seen_count[state] = 1

            for i in range(1, 11):
                new_state = state ^ 1 << i
                if new_state in state_seen_count:
                    res += state_seen_count[new_state]

        return res
