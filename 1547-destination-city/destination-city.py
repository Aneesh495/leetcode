class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        starts = {a for a, _ in paths}
        return next(b for _, b in paths if b not in starts)