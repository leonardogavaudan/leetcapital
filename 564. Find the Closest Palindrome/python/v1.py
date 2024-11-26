from typing import List


class Solution:
    def find_lower(self, arr: List[int]) -> int:
        left, right = len(arr) // 2 - int(len(arr) % 2 == 0), len(arr) // 2
        while left >= 0 and right < len(arr):
            if arr[left] == 0:
                arr[left] = arr[right] = 9
                left -= 1
                right += 1
            else:
                arr[right] = arr[left] = arr[left] - 1
                break

        if arr[0] == 0:
            return 10 ** (len(arr) - 1) - 1

        return int("".join(map(str, arr)))

    def find_higher(self, arr: List[int]) -> int:
        left, right = len(arr) // 2 - int(len(arr) % 2 == 0), len(arr) // 2
        while left >= 0 and right < len(arr):
            if arr[left] == 9:
                arr[left] = arr[right] = 0
                left -= 1
                right += 1
            else:
                arr[right] = arr[left] = arr[left] + 1
                break

        if left == -1:
            return 10 ** len(arr) + 1

        return int("".join(map(str, arr)))

    def nearestPalindromic(self, n: str) -> str:
        n_int = int(n)
        if n_int < 10:
            return str(n_int - 1)

        num_list = [int(c) for c in n]
        left, right = 0, len(num_list) - 1
        while left < right:
            num_list[right] = num_list[left]
            left += 1
            right -= 1

        num_int = int("".join(map(str, num_list)))
        if num_int < n_int:
            higher = self.find_higher(num_list[:])
            if higher - n_int < n_int - num_int:
                return str(higher)
            else:
                return str(num_int)
        elif num_int > n_int:
            lower = self.find_lower(num_list[:])
            if num_int - n_int < n_int - lower:
                return str(num_int)
            else:
                return str(lower)
        else:
            lower = self.find_lower(num_list[:])
            higher = self.find_higher(num_list[:])
            if higher - n_int < n_int - lower:
                return str(higher)
            else:
                return str(lower)
