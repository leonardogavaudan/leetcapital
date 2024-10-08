from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_num = 10**5
        max_num = 0
        for num in nums:
            if num > max_num:
                max_num = num
            if num < min_num:
                min_num = num

        count_arr = [0] * (max_num - min_num + 1)

        for num in nums:
            count_arr[num - min_num] += 1

        res = 0
        i = len(count_arr) - 1
        while res < k:
            res += count_arr[i]
            i -= 1

        return i + min_num + 1
