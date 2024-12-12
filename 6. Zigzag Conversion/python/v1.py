class Solution:
    def convert(self, s: str, numRows: int) -> str:
        arr = [[] for _ in range(numRows)]
        i = 0
        while i < len(s):
            j = 0
            while i < len(s) and j < numRows:
                arr[j].append(s[i])
                i += 1
                j += 1

            j = numRows - 2
            while i < len(s) and j > 0:
                arr[j].append(s[i])
                i += 1
                j -= 1

        return "".join(["".join(row) for row in arr])
