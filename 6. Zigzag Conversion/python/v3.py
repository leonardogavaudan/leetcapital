class Solution:
    def convert(self, s: str, numRows: int) -> str:
        res = [[] for _ in range(numRows)]
        i = 0
        while i < len(s):
            for row in range(numRows):
                if i == len(s):
                    break
                res[row].append(s[i])
                i += 1
            if i == len(s):
                break

            for row in range(numRows - 2, 0, -1):
                if i == len(s):
                    break
                res[row].append(s[i])
                i += 1

        return "".join(("".join(x) for x in res))
