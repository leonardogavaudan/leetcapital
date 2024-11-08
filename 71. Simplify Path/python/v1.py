class Solution:
    def simplifyPath(self, path: str) -> str:
        res = []
        i = 0
        while i < len(path) and path[i] == "/":
            i += 1

        while i < len(path):
            initial_position = i
            while i < len(path) and path[i] != "/":
                i += 1

            part = path[initial_position:i]
            if part == ".." and len(res) > 0:
                res.pop()

            if part not in [".", ".."]:
                res.append(part)

            while i < len(path) and path[i] == "/":
                i += 1

        return "/" + "/".join(res)
