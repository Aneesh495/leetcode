
from typing import List

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        # DSU over rows and columns. Use ~c to keep column keys disjoint from row keys.
        parent = {}
        rank = {}

        def find(x: int) -> int:
            # Initialize parent lazily
            if x not in parent:
                parent[x] = x
                rank[x] = 0
            # Path compression
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a: int, b: int) -> None:
            ra, rb = find(a), find(b)
            if ra == rb:
                return
            # Union by rank
            if rank[ra] < rank[rb]:
                ra, rb = rb, ra
            parent[rb] = ra
            if rank[ra] == rank[rb]:
                rank[ra] += 1

        # Union row node with column node for each stone
        for r, c in stones:
            union(r, ~c)

        # Number of connected components equals number of unique roots touched
        roots = set()
        for r, c in stones:
            roots.add(find(r))
            roots.add(find(~c))

        # Max removable stones = total stones minus number of components
        return len(stones) - len(roots)
