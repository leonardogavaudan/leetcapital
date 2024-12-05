class Solution:
    def minimumSteps(self, s: str) -> int:
        res = 0
        available_index = 0
        for i in range(len(s)):
            if s[i] == "0":
                res += i - available_index
                available_index += 1
        return res
