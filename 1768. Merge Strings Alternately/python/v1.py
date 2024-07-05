class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1_len = len(word1)
        word2_len = len(word2)
        i = 0
        j = 0
        res = ""

        while i < word1_len and j < word2_len:
            if (i + j) % 2 == 0:
                res += word1[i]
                i += 1
            else:
                res += word2[j]
                j += 1

        while i < word1_len:
            res += word1[i]
            i += 1

        while j < word2_len:
            res += word2[j]
            j += 1

        return res
