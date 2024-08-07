
class MyHashSet:
    def __init__(self):
        self._size = 1009  # prime bucket count
        self._buckets = [[] for _ in range(self._size)]

    def _idx(self, key: int) -> int:
        return key % self._size

    def add(self, key: int) -> None:
        b = self._buckets[self._idx(key)]
        for v in b:
            if v == key:
                return
        b.append(key)

    def remove(self, key: int) -> None:
        b = self._buckets[self._idx(key)]
        for i, v in enumerate(b):
            if v == key:
                b[i] = b[-1]
                b.pop()
                return

    def contains(self, key: int) -> bool:
        b = self._buckets[self._idx(key)]
        for v in b:
            if v == key:
                return True
        return False
