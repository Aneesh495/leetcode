
class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        seen = set()
        ans = []
        start = "0" * (n - 1)

        def dfs(node: str):
            for d in map(str, range(k)):
                edge = node + d
                if edge not in seen:
                    seen.add(edge)
                    dfs(edge[1:])
                    ans.append(d)

        dfs(start)
        return start + "".join(reversed(ans))
