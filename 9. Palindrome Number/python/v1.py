from collections import deque


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        queue = deque()
        while x != 0:
            queue.append(x % 10)
            x //= 10

        while len(queue) > 1:
            if queue.pop() != queue.popleft():
                return False

        return True
