from bisect import bisect_right

class TimeMap:
    def __init__(self):
        self.data: dict[str, tuple[list[int], list[str]]] = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.data:
            self.data[key] = ([], [])
        timestamps, values = self.data[key]
        timestamps.append(timestamp)
        values.append(value)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data:
            return ""
        timestamps, values = self.data[key]
        index = bisect_right(timestamps, timestamp) - 1
        if index < 0:
            return ""
        return values[index]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)