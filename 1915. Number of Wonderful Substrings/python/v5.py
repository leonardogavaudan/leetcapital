class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        res = 0
        state = 0
        state_to_count = {0: 1}
        char_to_shift = {
            "a": 0,
            "b": 1,
            "c": 2,
            "d": 3,
            "e": 4,
            "f": 5,
            "g": 6,
            "h": 7,
            "i": 8,
            "j": 9,
        }

        for char in word:
            if char in char_to_shift:
                state = state ^ 1 << char_to_shift[char]

            if state in state_to_count:
                res += state_to_count[state]
            else:
                state_to_count[state] = 0

            state_to_count[state] += 1

            for i in range(10):
                adjacent_state = state ^ 1 << i
                res += state_to_count.get(adjacent_state, 0)

        return res
