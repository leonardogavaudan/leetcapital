from collections import defaultdict, deque
from typing import List


class Solution:
    def numBusesToDestination(
        self, routes: List[List[int]], source: int, target: int
    ) -> int:
        if source == target:
            return 0

        stop_to_bus = defaultdict(list)
        for bus_id, stops in enumerate(routes):
            for stop in stops:
                stop_to_bus[stop].append(bus_id)

        queue = deque()
        if source in stop_to_bus:
            for bus in stop_to_bus[source]:
                queue.append((1, bus))
        else:
            return -1

        visited = set()
        while queue:
            bus_count, bus = queue.popleft()

            if target in routes[bus]:
                return bus_count

            for stop in routes[bus]:
                for bus_neighbor in stop_to_bus[stop]:
                    if bus_neighbor not in visited:
                        visited.add(bus_neighbor)
                        queue.append((bus_count + 1, bus_neighbor))

        return -1
