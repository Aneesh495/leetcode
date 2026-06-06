class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return 0

            gold = grid[r][c]
            grid[r][c] = 0  # mark visited

            best = 0
            best = max(best, dfs(r + 1, c))
            best = max(best, dfs(r - 1, c))
            best = max(best, dfs(r, c + 1))
            best = max(best, dfs(r, c - 1))

            grid[r][c] = gold  # backtrack
            return gold + best

        ans = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != 0:
                    ans = max(ans, dfs(r, c))

        return ans
