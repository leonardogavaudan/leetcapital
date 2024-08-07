from typing import Counter, List


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        max_value = max(nums)
        counter = Counter(nums)
        current_count = 0

        for i in range(max_value, -1, -1):
            if i in counter:
                current_count += counter[i]

            if current_count == i:
                return i

        return -1
