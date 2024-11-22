from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        x = 0
        while x < len(height) and not height[x]:
            x += 1
        if x == len(height):
            return 0

        water = 0
        stack = []
        x += 1
        while x < len(height):
            if height[x - 1] > height[x]:
                stack.append([x - 1, height[x - 1]])
            elif height[x - 1] < height[x]:
                if not stack:
                    x += 1
                    continue

                height_base = height[x - 1]
                height_gain = height[x] - height[x - 1]
                while height_gain and stack:
                    stack_x, stack_height = stack[-1]
                    height_to_add = min(height_gain, stack_height - height_base)

                    new_water = height_to_add * (x - stack_x - 1)
                    water += new_water

                    height_gain -= height_to_add
                    height_base += height_to_add

                    if height[x] >= stack_height:
                        stack.pop()

            x += 1

        return water
