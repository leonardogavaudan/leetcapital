from typing import List


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        res = 0
        modulo_count = {0: 1}
        sum = 0
        for num in nums:
            sum += num
            mod_res = sum % k
            if mod_res in modulo_count:
                res += modulo_count[mod_res]
            else:
                modulo_count[mod_res] = 0

            modulo_count[mod_res] += 1

        return res
