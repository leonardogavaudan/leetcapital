class Solution:
    def simplifyPath(self, path: str) -> str:
        res = []
        i = 0

        while i < len(path):
            while i < len(path) and path[i] == "/":
                i += 1
            if i == len(path):
                break

            initial_index = i
            while i < len(path) and path[i] != "/":
                i += 1

            directory_or_file = path[initial_index:i]
            if directory_or_file == ".":
                continue
            elif directory_or_file == "..":
                if len(res):
                    res.pop()
            else:
                res.append(directory_or_file)

        return "/" + "/".join(res)
