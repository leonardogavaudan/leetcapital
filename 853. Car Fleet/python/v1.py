from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combined = list(zip(position, speed))
        combined.sort(key=lambda x: x[0])
        position = [x[0] for x in combined]
        speed = [x[1] for x in combined]

        fleet_count = 0
        fleet_time = float("-inf")
        for i in range(len(position) - 1, -1, -1):
            time = (target - position[i]) / speed[i]
            if time > fleet_time:
                fleet_count += 1
                fleet_time = time

        return fleet_count
