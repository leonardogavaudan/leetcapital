from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums_set = set(nums)
        seen = set()
        max_count = 0

        for num in nums:
            seen.add(num)
            count = 1
            x = num - 1
            while x in nums_set and x not in seen:
                seen.add(x)
                x -= 1
                count += 1

            x = num + 1
            while x in nums_set and x not in seen:
                seen.add(x)
                x += 1
                count += 1

            if count > max_count:
                max_count = count

        return max_count
