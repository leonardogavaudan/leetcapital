class MinStack:
    def __init__(self):
        self.stack = []
        self.monotonic_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.monotonic_stack or val <= self.monotonic_stack[-1]:
            self.monotonic_stack.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.monotonic_stack[-1]:
            self.monotonic_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.monotonic_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
