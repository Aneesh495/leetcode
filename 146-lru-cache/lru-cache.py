class LRUCache:
    class Node:
        def __init__(self, key: int, value: int):
            self.key = key
            self.value = value
            self.prev = None
            self.next = None
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.nodes = {}
        self.front = self.Node(0, 0)
        self.back = self.Node(0, 0)
        self.front.next = self.back
        self.back.prev = self.front
    def _remove(self, node: "LRUCache.Node") -> None:
        previous = node.prev
        following = node.next
        previous.next = following
        following.prev = previous
    def _insert_at_front(self, node: "LRUCache.Node") -> None:
        first = self.front.next
        self.front.next = node
        node.prev = self.front
        node.next = first
        first.prev = node

    def get(self, key: int) -> int:
        if key not in self.nodes:
            return -1
        node = self.nodes[key]
        self._remove(node)
        self._insert_at_front(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.nodes:
            node = self.nodes[key]
            node.value = value
            self._remove(node)
            self._insert_at_front(node)
            return
        node = self.Node(key, value)
        self.nodes[key] = node
        self._insert_at_front(node)
        if len(self.nodes) > self.capacity:
            least_recently_used = self.back.prev
            self._remove(least_recently_used)
            del self.nodes[least_recently_used.key]      


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)