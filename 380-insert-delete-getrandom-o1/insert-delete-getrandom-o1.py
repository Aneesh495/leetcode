import random

class RandomizedSet:

    def __init__(self):
        self.values: list[int] = []
        self.index_by_value: dict[int, int] = {}

    def insert(self, val: int) -> bool:
        if val in self.index_by_value:
            return False
        self.index_by_value[val] = len(self.values)
        self.values.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.index_by_value:
            return False
        remove_index = self.index_by_value[val]
        last_value = self.values[-1]
        if remove_index != len(self.values) - 1:
            self.values[remove_index] = last_value
            self.index_by_value[last_value] = remove_index
        self.values.pop()
        del self.index_by_value[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.values)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()