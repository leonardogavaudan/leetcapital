from typing import List


class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        dp = [float("inf")] * (len(books) + 1)
        dp[0] = 0

        for i in range(len(books) + 1):
            width = 0
            height = 0
            j = i - 1
            while j >= 0 and width + books[j][0] <= shelfWidth:
                width += books[j][0]
                height = max(height, books[j][1])
                dp[i] = min(dp[i], dp[j] + height)
                j -= 1

        return int(dp[len(books)])
