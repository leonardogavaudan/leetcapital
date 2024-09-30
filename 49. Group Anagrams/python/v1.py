from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        str_to_index = {}

        for i in range(len(strs)):
            sorted_str = "".join(sorted(strs[i]))
            if sorted_str not in str_to_index:
                str_to_index[sorted_str] = len(res)
                res.append([strs[i]])
            else:
                res[str_to_index[sorted_str]].append(strs[i])

        return res
