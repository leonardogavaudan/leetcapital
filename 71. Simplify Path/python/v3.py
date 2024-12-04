class Solution:
    def simplifyPath(self, path: str) -> str:
        i = 1
        while i < len(path) and path[i] == "/":
            i += 1

        res = []
        while i < len(path):
            initial_i = i
            while i < len(path) and path[i] != "/":
                i += 1

            if path[initial_i:i] == ".":
                pass
            elif path[initial_i:i] == "..":
                if res:
                    res.pop()
            else:
                res.append(path[initial_i:i])

            while i < len(path) and path[i] == "/":
                i += 1

        return "/" + "/".join(res)
