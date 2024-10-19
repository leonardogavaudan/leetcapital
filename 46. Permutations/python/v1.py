from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        permutation = []
        used = [False] * len(nums)

        def backtrack():
            if len(permutation) == len(nums):
                res.append(permutation.copy())
                return

            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    permutation.append(nums[i])
                    backtrack()
                    permutation.pop()
                    used[i] = False

        backtrack()

        return res
