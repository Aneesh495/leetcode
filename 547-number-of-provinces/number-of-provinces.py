
from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # Number of cities
        n = len(isConnected)
        # Track visited cities
        visited = [False] * n
        provinces = 0

        # Depth first search over adjacency matrix using a stack
        def dfs(start: int) -> None:
            stack = [start]
            visited[start] = True
            while stack:
                city = stack.pop()
                # Explore all neighbors of current city
                for nei in range(n):
                    # 1 means a direct road between city and nei
                    if isConnected[city][nei] == 1 and not visited[nei]:
                        visited[nei] = True
                        stack.append(nei)

        # Each unvisited city starts a new province
        for i in range(n):
            if not visited[i]:
                provinces += 1
                dfs(i)

        return provinces
