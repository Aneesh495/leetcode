
class MapSum:

    def __init__(self):
        self.root = {"sum": 0, "next": {}}
        self.kv = {}

    def insert(self, key: str, val: int) -> None:
        delta = val - self.kv.get(key, 0)
        self.kv[key] = val
        node = self.root
        node["sum"] += delta
        for ch in key:
            if ch not in node["next"]:
                node["next"][ch] = {"sum": 0, "next": {}}
            node = node["next"][ch]
            node["sum"] += delta

    def sum(self, prefix: str) -> int:
        node = self.root
        for ch in prefix:
            if ch not in node["next"]:
                return 0
            node = node["next"][ch]
        return node["sum"]
