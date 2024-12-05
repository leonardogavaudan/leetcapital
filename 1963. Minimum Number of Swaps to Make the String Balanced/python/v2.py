class Solution:
    def minSwaps(self, s: str) -> int:
        count = 0
        for c in s:
            if c == "[":
                count += 1
            elif c == "]":
                count = max(0, count - 1)
        return count // 2 + int(count % 2 == 1)
