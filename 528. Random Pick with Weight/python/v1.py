import random
from typing import List


class Solution:
    def __init__(self, w: List[int]):
        self.cum_prob = []
        self.w = w

        total = 0
        for num in w:
            total += num
            self.cum_prob.append(total)

        for i in range(len(w)):
            self.cum_prob[i] /= total

    def pickIndex(self) -> int:
        rand = random.random()

        l, r = 0, len(self.w) - 1

        while l <= r:
            mid = (l + r) // 2
            if self.cum_prob[mid] < rand:
                l = mid + 1
            else:
                r = mid - 1

        return l


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
