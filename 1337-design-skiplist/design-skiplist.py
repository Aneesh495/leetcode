import random

class Node:
    def __init__(self, val: int, level: int):
        self.val = val
        self.forward = [None] * level


class Skiplist:
    MAX_LEVEL = 16
    P = 0.5

    def __init__(self):
        self.head = Node(-1, self.MAX_LEVEL)
        self.level = 1

    def _random_level(self) -> int:
        lvl = 1
        while lvl < self.MAX_LEVEL and random.random() < self.P:
            lvl += 1
        return lvl

    def search(self, target: int) -> bool:
        curr = self.head
        for i in range(self.level - 1, -1, -1):
            while curr.forward[i] and curr.forward[i].val < target:
                curr = curr.forward[i]
        curr = curr.forward[0]
        return curr is not None and curr.val == target

    def add(self, num: int) -> None:
        update = [None] * self.MAX_LEVEL
        curr = self.head

        for i in range(self.level - 1, -1, -1):
            while curr.forward[i] and curr.forward[i].val < num:
                curr = curr.forward[i]
            update[i] = curr

        lvl = self._random_level()
        if lvl > self.level:
            for i in range(self.level, lvl):
                update[i] = self.head
            self.level = lvl

        node = Node(num, lvl)
        for i in range(lvl):
            node.forward[i] = update[i].forward[i]
            update[i].forward[i] = node

    def erase(self, num: int) -> bool:
        update = [None] * self.MAX_LEVEL
        curr = self.head

        for i in range(self.level - 1, -1, -1):
            while curr.forward[i] and curr.forward[i].val < num:
                curr = curr.forward[i]
            update[i] = curr

        curr = curr.forward[0]
        if curr is None or curr.val != num:
            return False

        for i in range(self.level):
            if update[i].forward[i] != curr:
                break
            update[i].forward[i] = curr.forward[i]

        while self.level > 1 and self.head.forward[self.level - 1] is None:
            self.level -= 1

        return True

# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)
