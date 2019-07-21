
# Below is the implementation for LeetCode 284 Peeking Iterator
# Assumes an existing Iterator class with next() and hasNext()

class PeekingIterator:
    def __init__(self, iterator):
        # Store the underlying iterator
        self.it = iterator
        # Preload the next value to enable O(1) peek
        if self.it.hasNext():
            self._has = True
            self._peek = self.it.next()
        else:
            self._has = False
            self._peek = None

    def peek(self):
        # Return the buffered value without advancing
        return self._peek

    def next(self):
        # Return the current buffered value and advance the buffer
        curr = self._peek
        if self.it.hasNext():
            self._peek = self.it.next()
            self._has = True
        else:
            self._peek = None
            self._has = False
        return curr

    def hasNext(self):
        # True if the buffer holds a value
        return self._has
