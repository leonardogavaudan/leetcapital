class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        total_1_count = 0

        for c in s:
            if c == "1":
                total_1_count += 1

        return (total_1_count - 1) * "1" + (len(s) - total_1_count) * "0" + "1"
