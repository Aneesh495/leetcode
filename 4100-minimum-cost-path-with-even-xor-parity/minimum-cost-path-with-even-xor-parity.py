class Solution:
    def minActivationCost(self, edges: list[list[int]], values: list[int]) -> int:
        size = len(values)
        graph = [[] for _ in values]
        for a, b, cost in edges:
            graph[a].append((b, cost))
            graph[b].append((a, cost))
        parent = [-1] * size
        edge_cost = [0] * size
        order = [0]
        for node in order:
            for child, cost in graph[node]:
                if child != parent[node]:
                    parent[child] = node
                    edge_cost[child] = cost
                    order.append(child)

        infinity = 10 ** 25
        parity = [value.bit_count() & 1 for value in values]
        down = [[0, infinity] if bit == 0 else [infinity, 0] for bit in parity]
        best = infinity
        for child in reversed(order[1:]):
            node = parent[child]
            cost = edge_cost[child]
            # Joining equal parity routes gives an even XOR across the connecting edge.
            best = min(best, down[node][0] + cost + down[child][0],
                       down[node][1] + cost + down[child][1])
            for child_bit in range(2):
                bit = child_bit ^ parity[node]
                down[node][bit] = min(down[node][bit], cost + down[child][child_bit])
        return -1 if best == infinity else best