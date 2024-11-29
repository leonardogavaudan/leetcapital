from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def heapify(arr: List[int], i: int, n: int):
            largest = i
            left = i * 2 + 1
            right = i * 2 + 2

            if left < n and nums[left] > nums[largest]:
                largest = left
            if right < n and nums[right] > nums[largest]:
                largest = right

            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]
                heapify(arr, largest, n)

        for i in range((len(nums) - 1) // 2, -1, -1):
            heapify(nums, i, len(nums))

        for i in range(len(nums) - 1, 0, -1):
            nums[i], nums[0] = nums[0], nums[i]
            heapify(nums, 0, i)

        return nums
