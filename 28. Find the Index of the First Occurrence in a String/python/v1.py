class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i, j = 0, 0
        index_res = 0

        while i <= len(haystack) - 1 and j <= len(needle) - 1:
            if haystack[i] == needle[j]:
                if j == len(needle) - 1:
                    return index_res

                i += 1
                j += 1
            else:
                i += 1
                j = 0

                index_res = i

        return -1
