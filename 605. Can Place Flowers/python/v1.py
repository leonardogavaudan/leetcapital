from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        total = 0

        while i < len(flowerbed):
            left_unoccupied = i - 1 < 0 or flowerbed[i] == 0
            right_unoccupied = i + 1 > len(flowerbed) or flowerbed[i] == 0
            if left_unoccupied and right_unoccupied:
                total += 1
                flower_bed[i] = 1
                i += 2
            else:
                i += 1
