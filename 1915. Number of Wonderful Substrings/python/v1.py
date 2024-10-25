class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        res = 0
        char_count = {}
        odd_count = 0

        def backtracking(position: int):
            nonlocal res, char_count, odd_count

            if position >= len(word):
                return

            backtracking(position + 1)

            original_char_count = char_count.copy()
            original_odd_count = odd_count

            for i in range(position, len(word)):
                if word[i] not in char_count:
                    char_count[word[i]] = 0
                char_count[word[i]] += 1

                if char_count[word[i]] % 2 == 1:
                    odd_count += 1
                else:
                    odd_count -= 1

                if odd_count < 2:
                    res += 1

            char_count = original_char_count
            odd_count = original_odd_count

        backtracking(0)

        return res
