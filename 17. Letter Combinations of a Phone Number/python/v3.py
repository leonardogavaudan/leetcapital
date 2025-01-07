from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        dp = [set() for _ in range(len(digits) + 1)]
        dp[0] = set([""])
        digit_to_char = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        for i in range(1, len(digits) + 1):
            digit = digits[i - 1]
            for x in dp[i - 1]:
                for char in digit_to_char[digit]:
                    dp[i].add(x + char)

        return list(dp[-1])
