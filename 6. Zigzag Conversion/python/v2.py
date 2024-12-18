from functools import reduce


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        arr = [[] for _ in range(numRows)]
        row = 0
        i = 0
        while i < len(s):
            for row in range(0, numRows):
                if i >= len(s):
                    break
                arr[row].append(s[i])
                i += 1

            for row in range(numRows - 2, 0, -1):
                if i >= len(s):
                    break
                arr[row].append(s[i])
                i += 1

        return reduce(lambda x, y: x + "".join(y), arr, "")
