import random


class RandomizedSet:

    def __init__(self):
        self.values = []
        self.val_to_index = {}

    def insert(self, val: int) -> bool:
        if val in self.val_to_index:
            return False

        self.values.append(val)
        self.val_to_index[val] = len(self.values) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_to_index:
            return False

        last_value = self.values[-1]
        self.values[self.val_to_index[val]] = last_value
        self.val_to_index[last_value] = self.val_to_index[val]

        del self.val_to_index[val]
        self.values.pop()

        return True

    def getRandom(self) -> int:
        random_index = random.randint(0, len(self.values) - 1)
        return self.values[random_index]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
