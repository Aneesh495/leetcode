
from collections import defaultdict
import bisect

class TimeMap:
    """
    Time based key value store.
    set stores (timestamp, value) per key
    get returns the value with the largest timestamp <= query time or "" if none
    """

    def __init__(self):
        # key -> list of (timestamp, value). Timestamps for a given key are added in increasing order
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # Append since timestamps for a key are strictly increasing per problem statement
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        pairs = self.store.get(key, [])
        if not pairs:
            return ""
        # Binary search for rightmost timestamp <= query time
        # Use tuple order so (timestamp, chr(127)) acts as an upper bound for all values at that timestamp
        idx = bisect.bisect_right(pairs, (timestamp, chr(127))) - 1
        return pairs[idx][1] if idx >= 0 else ""
