from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def heapify(arr: List[int], size: int, i: int):
            left, right = i * 2 + 1, i * 2 + 2
            largest = i
            if left < size and arr[left] > arr[largest]:
                largest = left
            if right < size and arr[right] > arr[largest]:
                largest = right

            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]
                heapify(arr, size, largest)

        for i in range(len(nums) // 2 - 1, -1, -1):
            heapify(nums, len(nums), i)

        for i in range(len(nums)):
            nums[len(nums) - 1 - i], nums[0] = nums[0], nums[len(nums) - 1 - i]
            heapify(nums, len(nums) - 1 - i, 0)

        return nums
