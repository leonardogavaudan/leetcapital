from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        target_index = len(nums) - k

        def quick_select(l: int, r: int) -> int:
            final_pivot_index = l
            pivot = nums[r]

            for i in range(l, r):
                if nums[i] < pivot:
                    nums[final_pivot_index], nums[i] = nums[i], nums[final_pivot_index]
                    final_pivot_index += 1

            nums[final_pivot_index], nums[r] = nums[r], nums[final_pivot_index]

            if target_index < final_pivot_index:
                return quick_select(l, final_pivot_index - 1)
            elif target_index > final_pivot_index:
                return quick_select(final_pivot_index + 1, r)
            else:
                return nums[final_pivot_index]

        return quick_select(0, len(nums) - 1)
