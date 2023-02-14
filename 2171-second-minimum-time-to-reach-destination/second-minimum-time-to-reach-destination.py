class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u - 1].append(v - 1)
            graph[v - 1].append(u - 1)
        dist = [[-1, -1] for _ in range(n)]
        dist[0][0] = 0
        queue = [(0, 0)]
        head = 0
        while head < len(queue):
            node, steps = queue[head]
            head += 1
            for nxt in graph[node]:
                candidate = steps + 1
                if dist[nxt][0] == -1:
                    dist[nxt][0] = candidate
                    queue.append((nxt, candidate))
                elif dist[nxt][1] == -1 and candidate != dist[nxt][0]:
                    dist[nxt][1] = candidate
                    queue.append((nxt, candidate))
        elapsed = 0
        for _ in range(dist[n - 1][1]):
            if (elapsed // change) % 2 == 1:
                elapsed = ((elapsed // change) + 1) * change
            elapsed += time
        return elapsed