import random


class RandomizedSet:

    def __init__(self):
        self.val_to_index = {}
        self.arr = []

    def insert(self, val: int) -> bool:
        if val in self.val_to_index:
            return False

        self.arr.append(val)
        self.val_to_index[val] = len(self.arr) - 1

        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_to_index:
            return False

        last_element = self.arr[-1]
        self.arr[self.val_to_index[val]] = last_element
        self.arr.pop()
        self.val_to_index[last_element] = self.val_to_index[val]
        del self.val_to_index[val]

        return True

    def getRandom(self) -> int:
        return self.arr[random.randint(0, len(self.arr) - 1)]
