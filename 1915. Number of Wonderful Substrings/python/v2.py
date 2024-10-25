class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        res = 0
        char_count = {}
        odd_count = 0

        for i in range(len(word)):
            original_char_count = char_count.copy()
            original_odd_count = 0

            for j in range(i, len(word)):
                if word[j] not in char_count:
                    char_count[word[j]] = 0

                char_count[word[j]] += 1

                if char_count[word[j]] % 2 == 0:
                    odd_count -= 1
                else:
                    odd_count += 1

                if odd_count < 2:
                    res += 1

            char_count = original_char_count
            odd_count = original_odd_count

        return res
