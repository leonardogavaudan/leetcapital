class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        if s == goal:
            return True

        for offset in range(len(s)):
            if s == goal[offset:] + goal[:offset]:
                return True

        return False 
