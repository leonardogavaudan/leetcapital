from typing import List


class Solution:
    def survivedRobotsHealths(
        self, positions: List[int], healths: List[int], directions: str
    ) -> List[int]:
        bots = [
            {
                "position": positions[i],
                "health": healths[i] * (1 if directions[i] == "R" else -1),
                "original_position": i,
            }
            for i in range(len(positions))
        ]
        bots.sort(key=lambda x: x["position"])

        stack = []

        for bot in bots:
            while stack and bot["health"] < 0 < stack[-1]["health"]:
                if abs(bot["health"]) > stack[-1]["health"]:
                    stack.pop()
                    bot["health"] += 1
                elif abs(bot["health"]) < stack[-1]["health"]:
                    stack[-1]["health"] -= 1
                    break
                else:
                    stack.pop()
                    break
            else:
                stack.append(bot)

        return list(
            map(
                lambda x: abs(x["health"]),
                sorted(stack, key=lambda x: x["original_position"]),
            )
        )
