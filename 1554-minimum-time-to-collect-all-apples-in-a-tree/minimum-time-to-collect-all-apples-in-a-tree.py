class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = [[] for _ in range(n)]
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        parent = [-1] * n
        order = [0]
        for u in order:
            for v in graph[u]:
                if v != parent[u]:
                    parent[v] = u
                    order.append(v)
        needed = hasApple[:]
        result = 0
        for u in reversed(order[1:]):
            if needed[u]:
                result += 2
                needed[parent[u]] = True
        return result