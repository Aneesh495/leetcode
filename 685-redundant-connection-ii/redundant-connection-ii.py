
class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [0] * (n + 1)
        cand1 = cand2 = None

        # Step 1: check whether there is a node with two parents
        for u, v in edges:
            if parent[v] == 0:
                parent[v] = u
            else:
                cand1 = [parent[v], v]
                cand2 = [u, v]
                break

        # Union-Find
        def find(x, fa):
            while fa[x] != x:
                fa[x] = fa[fa[x]]
                x = fa[x]
            return x

        def union(x, y, fa):
            rx, ry = find(x, fa), find(y, fa)
            if rx == ry:
                return False
            fa[ry] = rx
            return True

        # Step 2: try to build tree, skip cand2 if exists
        fa = list(range(n + 1))
        for u, v in edges:
            if cand2 and [u, v] == cand2:
                continue
            if not union(u, v, fa):
                # found cycle
                return cand1 if cand1 else [u, v]

        # If no cycle found when skipping cand2, then cand2 is the answer
        return cand2
