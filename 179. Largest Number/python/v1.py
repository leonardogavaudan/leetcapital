from typing import List


class Solution:

    def largestNumber(self, nums: List[int]) -> str:
        res = nums.copy()

        def compare(num1: int, num2: int) -> int:
            if num1 == num2:
                return 1
            if not num1:
                return 0
            if not num2:
                return 1

            stack1 = []
            stack2 = []
            while num1:
                stack1.append(num1 % 10)
                num1 //= 10
            while num2:
                stack2.append(num2 % 10)
                num2 //= 10

            l1, l2 = stack1[::-1] + stack2[::-1], stack2[::-1] + stack1[::-1]
            for i in range(len(l1)):
                if l1[i] > l2[i]:
                    return 1
                if l2[i] > l1[i]:
                    return 0

            return 1

        def partition(arr: List[int], low: int, high: int) -> int:
            final_pivot_index = low
            pivot = arr[high]

            for i in range(low, high):
                if compare(arr[i], pivot):
                    arr[i], arr[final_pivot_index] = arr[final_pivot_index], arr[i]
                    final_pivot_index += 1

            arr[final_pivot_index], arr[high] = arr[high], arr[final_pivot_index]

            return final_pivot_index

        def quick_sort(arr: List[int], low: int, high: int) -> None:
            if low < high:
                i = partition(arr, low, high)
                quick_sort(arr, low, i - 1)
                quick_sort(arr, i + 1, high)

        quick_sort(res, 0, len(res) - 1)

        return str(int("".join(str(x) for x in res)))
