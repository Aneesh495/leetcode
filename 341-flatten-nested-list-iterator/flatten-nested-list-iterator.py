
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# class NestedInteger:
#     def isInteger(self) -> bool: ...
#     def getInteger(self) -> int: ...
#     def getList(self) -> [NestedInteger]: ...
# """

from typing import List

class NestedIterator:
    def __init__(self, nestedList: List['NestedInteger']):
        self.stack = list(reversed(nestedList))  # use stack of NestedInteger

    def next(self) -> int:
        self.hasNext()  # ensure top is integer
        return self.stack.pop().getInteger()

    def hasNext(self) -> bool:
        while self.stack:
            top = self.stack[-1]
            if top.isInteger():
                return True
            self.stack.pop()
            self.stack.extend(reversed(top.getList()))
        return False
