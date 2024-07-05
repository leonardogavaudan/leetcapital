from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for s in strs[1:]:
            max_size = min(len(prefix), len(s))
            new_prefix_size = 0
            for i in range(max_size):
                if prefix[i] != s[i]:
                    break
                new_prefix_size += 1
            prefix = prefix[:new_prefix_size]

        return prefix
