from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        l, r = 0, len(arr) - 1
        index = 0
        missing_numbers_count = 0

        while l <= r:
            index = (l + r) // 2
            missing_numbers_count = arr[index] - (index + 1)

            if missing_numbers_count < k:
                l = index + 1
            elif missing_numbers_count > k:
                r = index - 1
            else:
                r = index - 1

        if missing_numbers_count >= k:
            return arr[index] - (missing_numbers_count - k) - 1
        else:
            return arr[index] + k - missing_numbers_count
