
from typing import List

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph) - 1
        res = []
        path = [0]

        def dfs(node: int) -> None:
            if node == target:
                res.append(path.copy())
                return
            for nei in graph[node]:
                path.append(nei)
                dfs(nei)
                path.pop()

        dfs(0)
        return res
