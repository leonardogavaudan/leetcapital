from collections import deque


class HitCounter:

    def __init__(self):
        self.total = 0
        self.queue = deque()

    def _clean(self, timestamp: int):
        while self.queue and self.queue[0][0] < timestamp - 299:
            self.total -= self.queue.popleft()[1]

    def hit(self, timestamp: int) -> None:
        if self.queue and self.queue[-1][0] == timestamp:
            self.queue[-1][1] += 1
        else:
            self.queue.append([timestamp, 1])
        self.total += 1
        self._clean(timestamp)

    def getHits(self, timestamp: int) -> int:
        self._clean(timestamp)
        return self.total
