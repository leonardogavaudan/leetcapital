import collections
from typing import List


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        sorted_deck = sorted(deck)
        queue = collections.deque([sorted_deck[-1]])

        for i in range(len(sorted_deck) - 2, -1, -1):
            queue.appendleft(queue.pop())
            queue.appendleft(sorted_deck[i])

        return list(queue)
