
from typing import List

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # Union-Find with weights
        # parent[x] gives x's parent
        # weight[x] stores the ratio x / parent[x]
        parent = {}
        weight = {}

        def add(x: str) -> None:
            if x not in parent:
                parent[x] = x
                weight[x] = 1.0

        def find(x: str) -> str:
            # Path compression with weight update
            if parent[x] != x:
                root = find(parent[x])
                weight[x] *= weight[parent[x]]
                parent[x] = root
            return parent[x]

        def union(x: str, y: str, val: float) -> None:
            # Enforce x / y = val
            add(x)
            add(y)
            rx = find(x)
            ry = find(y)
            if rx == ry:
                return
            # Connect rx under ry
            # We want: weight[x] * (rx/?) ... derive:
            # x = weight[x] * parent[x]
            # After find, x/rv = weight[x], y/rv = weight[y] where rv is root
            # To satisfy x / y = val when linking rx -> ry:
            # weight[rx] should make (x/ry) / (y/ry) = val
            # x/ry = weight[x] * weight[rx]
            # y/ry = weight[y]
            # So weight[rx] = val * weight[y] / weight[x]
            parent[rx] = ry
            weight[rx] = val * weight[y] / weight[x]

        # Build the structure
        for (a, b), v in zip(equations, values):
            union(a, b, v)

        # Answer queries
        ans = []
        for a, b in queries:
            if a not in parent or b not in parent:
                ans.append(-1.0)
                continue
            ra = find(a)
            rb = find(b)
            if ra != rb:
                ans.append(-1.0)
            else:
                # a / b = (a/root) / (b/root) = weight[a] / weight[b]
                ans.append(weight[a] / weight[b])
        return ans
