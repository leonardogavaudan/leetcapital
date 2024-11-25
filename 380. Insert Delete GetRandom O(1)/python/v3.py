import random


class RandomizedSet:

    def __init__(self):
        self.arr = []
        self.num_to_index = {}

    def insert(self, val: int) -> bool:
        if val in self.num_to_index:
            return False

        self.arr.append(val)
        self.num_to_index[val] = len(self.arr) - 1

        return True

    def remove(self, val: int) -> bool:
        if val not in self.num_to_index:
            return False

        self.arr[self.num_to_index[val]] = self.arr[-1]
        self.num_to_index[self.arr[-1]] = self.num_to_index[val]
        del self.num_to_index[val]
        self.arr.pop()

        return True

    def getRandom(self) -> int:
        return self.arr[random.randint(0, len(self.arr) - 1)]
