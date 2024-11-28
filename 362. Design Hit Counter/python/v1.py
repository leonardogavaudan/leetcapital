from collections import deque


class HitCounter:

    def __init__(self):
        self.queue = deque([])
        self.total_hits = 0

    def clean(self, timestamp: int):
        while self.queue and self.queue[0][0] < timestamp - 299:
            _, hits = self.queue.popleft()
            self.total_hits -= hits

    def hit(self, timestamp: int) -> None:
        self.clean(timestamp)
        if self.queue and self.queue[-1][0] == timestamp:
            self.queue[-1][1] += 1
        else:
            self.queue.append([timestamp, 1])
        self.total_hits += 1

    def getHits(self, timestamp: int) -> int:
        self.clean(timestamp)
        return self.total_hits
