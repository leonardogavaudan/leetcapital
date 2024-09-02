from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        total = 0

        while i < len(flowerbed):
            left_unoccupied = i - 1 < 0 or flowerbed[i - 1] == 0
            right_unoccupied = i + 1 > len(flowerbed) - 1 or flowerbed[i + 1] == 0
            if flowerbed[i] == 0 and left_unoccupied and right_unoccupied:
                total += 1
                flowerbed[i] = 1
                i += 2
            else:
                i += 1

        return total >= n
