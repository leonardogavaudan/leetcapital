from collections import defaultdict, deque
from typing import List


class Solution:
    def numBusesToDestination(
        self, routes: List[List[int]], source: int, target: int
    ) -> int:
        if source == target:
            return 0

        stop_to_bus = defaultdict(list)
        queue = deque()
        seen = set()

        for bus, route in enumerate(routes):
            for stop in route:
                stop_to_bus[stop].append(bus)
                if stop == source:
                    queue.append((bus, 1))
                    seen.add(bus)

        while queue:
            bus, bus_count = queue.popleft()
            if target in routes[bus]:
                return bus_count

            for stop in routes[bus]:
                for bus_neighbor in stop_to_bus[stop]:
                    if bus_neighbor not in seen:
                        seen.add(bus_neighbor)
                        queue.append((bus_neighbor, bus_count + 1))

        return -1
