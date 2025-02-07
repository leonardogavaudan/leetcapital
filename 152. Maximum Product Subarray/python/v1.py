from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        def search(candidate, start, end):
            if start == end:
                return candidate

            j = start
            candidate_1 = candidate
            while candidate_1 < 0:
                if j == len(nums) or nums[j] == 0:
                    break
                candidate_1 /= nums[j]
                j += 1

            j = end
            candidate_2 = candidate
            while candidate_2 < 0:
                if j == -1 or nums[j] == 0:
                    break
                candidate_2 /= nums[j]
                j -= 1

            return max(candidate_1, candidate_2)

        max_product = max(nums)
        curr_product = 1
        start = 0
        nums.append(0)
        for i in range(len(nums)):
            if nums[i] != 0:
                curr_product *= nums[i]
                max_product = max(max_product, curr_product)
            else:
                if curr_product < 0:
                    max_product = max(max_product, search(curr_product, start, i - 1))
                start = i + 1
                curr_product = 1

        return int(max_product)
