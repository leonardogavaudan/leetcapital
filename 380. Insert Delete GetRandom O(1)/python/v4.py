from random import randint


class RandomizedSet:
    def __init__(self):
        self.arr = []
        self.num_to_index = {}

    def insert(self, val: int) -> bool:
        if val in self.num_to_index:
            return False
        self.num_to_index[val] = len(self.arr)
        self.arr.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.num_to_index:
            return False
        index = self.num_to_index[val]

        new_val = self.arr[index] = self.arr[-1]
        self.arr.pop()

        self.num_to_index[new_val] = index
        del self.num_to_index[val]

        return True

    def getRandom(self) -> int:
        return self.arr[randint(0, len(self.arr) - 1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
