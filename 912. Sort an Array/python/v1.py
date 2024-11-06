from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def heapify(nums: List[int], n: int, i: int):
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2

            if left < n and nums[left] > nums[largest]:
                largest = left

            if right < n and nums[right] > nums[largest]:
                largest = right

            if largest != i:
                nums[i], nums[largest] = nums[largest], nums[i]
                heapify(nums, n, largest)

        for i in range(len(nums) // 2 - 1, -1, -1):
            heapify(nums, len(nums), i)

        for i in range(len(nums) - 1, -1, -1):
            nums[0], nums[i] = nums[i], nums[0]
            heapify(nums, i, 0)

        return nums
