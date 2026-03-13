
class Node:
    def __init__(self, val=0, nxt=None):
        self.val = val
        self.next = nxt

class MyLinkedList:

    def __init__(self):
        self.head = Node(0)  # sentinel
        self.tail = self.head
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        curr = self.head.next
        for _ in range(index):
            curr = curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:
        node = Node(val, self.head.next)
        self.head.next = node
        if self.size == 0:
            self.tail = node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        node = Node(val)
        if self.size == 0:
            self.head.next = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0:
            index = 0
        if index > self.size:
            return
        if index == self.size:
            self.addAtTail(val)
            return
        prev = self.head
        for _ in range(index):
            prev = prev.next
        node = Node(val, prev.next)
        prev.next = node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        prev = self.head
        for _ in range(index):
            prev = prev.next
        to_delete = prev.next
        prev.next = to_delete.next
        if index == self.size - 1:
            self.tail = prev
        self.size -= 1
