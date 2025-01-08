from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            if not stack:
                stack.append(a)
                continue

            if a < 0 and stack and stack[-1] > 0:
                while stack and stack[-1] > 0:
                    if abs(a) > stack[-1]:
                        stack.pop()
                        if not stack or stack[-1] < 0:
                            stack.append(a)
                    elif abs(a) < stack[-1]:
                        break
                    else:
                        stack.pop()
                        break
            else:
                stack.append(a)
        return stack
