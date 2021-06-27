from typing import List
from collections import defaultdict, deque

class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        for i in range(n):
            if group[i] == -1:
                group[i] = m
                m += 1

        item_graph = [[] for _ in range(n)]
        item_indeg = [0] * n

        group_graph = [[] for _ in range(m)]
        group_indeg = [0] * m

        for v in range(n):
            for u in beforeItems[v]:
                item_graph[u].append(v)
                item_indeg[v] += 1

                if group[u] != group[v]:
                    group_graph[group[u]].append(group[v])
                    group_indeg[group[v]] += 1

        def topo(graph, indeg):
            q = deque([i for i in range(len(indeg)) if indeg[i] == 0])
            order = []

            while q:
                u = q.popleft()
                order.append(u)
                for v in graph[u]:
                    indeg[v] -= 1
                    if indeg[v] == 0:
                        q.append(v)

            return order if len(order) == len(indeg) else []

        item_order = topo(item_graph, item_indeg)
        if not item_order:
            return []

        group_order = topo(group_graph, group_indeg)
        if not group_order:
            return []

        items_in_group = defaultdict(list)
        for item in item_order:
            items_in_group[group[item]].append(item)

        ans = []
        for g in group_order:
            ans.extend(items_in_group[g])

        return ans
