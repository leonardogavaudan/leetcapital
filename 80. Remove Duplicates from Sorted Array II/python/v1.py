from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ptr1 = 0
        count = 1
        for ptr2 in range(1, len(nums)):
            if nums[ptr1] != nums[ptr2] or count < 2:
                if nums[ptr1] != nums[ptr2]:
                    count = 1
                else:
                    count = 2

                ptr1 += 1
                nums[ptr1] = nums[ptr2]

        return ptr1 + 1
