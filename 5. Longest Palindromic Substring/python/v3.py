class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = s[0]

        dp = [[0] * len(s) for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = 1

        for str_len in range(2, len(s) + 1):
            for starting_index in range(0, len(s) - str_len + 1):
                ending_index = starting_index + str_len - 1
                if (str_len == 2 or dp[starting_index + 1][ending_index - 1]) and s[
                    starting_index
                ] == s[ending_index]:
                    dp[starting_index][ending_index] = 1
                    if ending_index - starting_index + 1 > len(res):
                        res = s[starting_index : ending_index + 1]

        return res
