
import random

class RandomizedSet:
    def __init__(self):
        # arr stores values so we can get a random element in O(1)
        # pos maps value to its index in arr for O(1) insert and remove
        self.arr = []
        self.pos = {}

    def insert(self, val: int) -> bool:
        # Return False if already present
        if val in self.pos:
            return False
        # Append to arr and record its index
        self.pos[val] = len(self.arr)
        self.arr.append(val)
        return True

    def remove(self, val: int) -> bool:
        # Return False if not present
        if val not in self.pos:
            return False
        # Index of element to remove
        idx = self.pos[val]
        # Move last element into idx to keep array compact
        last_val = self.arr[-1]
        self.arr[idx] = last_val
        self.pos[last_val] = idx
        # Remove last element from arr and delete mapping
        self.arr.pop()
        del self.pos[val]
        return True

    def getRandom(self) -> int:
        # Each element has equal probability
        return self.arr[random.randrange(len(self.arr))]
