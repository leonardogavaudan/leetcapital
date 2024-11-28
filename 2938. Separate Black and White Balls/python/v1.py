class Solution:
    def minimumSteps(self, s: str) -> int:
        steps = 0
        available_position = 0
        for i in range(len(s)):
            if s[i] == "1":
                steps += i - available_position
                available_position += 1
