
from collections import defaultdict, OrderedDict

class LFUCache:
    """
    LFU Cache with O(1) get and put on average.
    Uses two maps:
      1. key_to_val_freq maps key to [value, freq]
      2. freq_to_lru maps freq to an OrderedDict that stores keys for LRU within same freq
    Maintains min_freq to know which list to evict from.
    """

    def __init__(self, capacity: int):
        self.cap = capacity
        self.size = 0
        self.min_freq = 0
        self.key_to_val_freq = {}                          # key -> [value, freq]
        self.freq_to_lru = defaultdict(OrderedDict)        # freq -> OrderedDict of keys for LRU

    def _touch(self, key: int) -> None:
        """
        Move existing key to next freq and update LRU structures.
        """
        val, freq = self.key_to_val_freq[key]
        # remove from current freq LRU
        lru = self.freq_to_lru[freq]
        if key in lru:
            lru.pop(key)
        # if current freq list is now empty and was the min freq then bump min freq
        if not lru and self.min_freq == freq:
            self.min_freq += 1
        # add to next freq LRU at the end which is most recent for that freq
        new_freq = freq + 1
        self.freq_to_lru[new_freq][key] = None
        # write back new freq
        self.key_to_val_freq[key][1] = new_freq

    def get(self, key: int) -> int:
        if key not in self.key_to_val_freq:
            return -1
        self._touch(key)
        return self.key_to_val_freq[key][0]

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return
        if key in self.key_to_val_freq:
            # update value then touch to raise freq and position
            self.key_to_val_freq[key][0] = value
            self._touch(key)
            return

        # need to insert a new key. evict if at capacity
        if self.size == self.cap:
            # evict least freq and least recent in that freq
            lru = self.freq_to_lru[self.min_freq]
            evict_key, _ = lru.popitem(last=False)
            del self.key_to_val_freq[evict_key]
            self.size -= 1

        # insert new key with freq 1
        self.key_to_val_freq[key] = [value, 1]
        self.freq_to_lru[1][key] = None
        self.min_freq = 1
        self.size += 1
