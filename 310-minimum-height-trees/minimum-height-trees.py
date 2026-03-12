
from collections import deque, defaultdict
from typing import List

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # Handle small trees directly
        if n <= 2:
            # All nodes are centroids when the node count is 1 or 2
            return list(range(n))

        # Build an adjacency list and a degree array
        graph = defaultdict(set)  # Each node maps to the set of its neighbors
        degree = [0] * n          # Degree of each node

        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
            degree[u] += 1
            degree[v] += 1

        # Initialize the first layer of leaves
        leaves = deque([i for i in range(n) if degree[i] == 1])

        # Number of nodes that still remain
        remaining = n

        # Trim leaves layer by layer until at most two nodes remain
        while remaining > 2:
            leaf_count = len(leaves)
            remaining -= leaf_count

            for _ in range(leaf_count):
                leaf = leaves.popleft()
                # Each leaf has exactly one neighbor in a tree
                for nei in list(graph[leaf]):
                    # Remove the edge leaf to neighbor
                    graph[nei].remove(leaf)
                    degree[nei] -= 1
                    if degree[nei] == 1:
                        # This neighbor becomes a new leaf
                        leaves.append(nei)
                # Clear neighbors of the processed leaf to free memory
                graph[leaf].clear()

        # The remaining one or two nodes are the centroids
        return list(leaves) if leaves else [0]
