class MovingAverage:
    def __init__(self, size: int):
        self.max_window_size = size
        self.current_window_size = 0
        self.window = []
        self.window_sum = 0

    def next(self, val: int) -> float:
        self.window.append(val)
        self.window_sum += val

        if self.current_window_size >= self.max_window_size:
            self.window_sum -= self.window.pop(0)
        else:
            self.current_window_size += 1

        return self.window_sum / self.current_window_size
