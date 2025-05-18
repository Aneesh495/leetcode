class Solution:
    def maxSum(self, grid: list[list[int]], limits: list[int], k: int) -> int:
        eligible = []
        for row, limit in zip(grid, limits):
            # Only the largest allowed values in each row can help the optimum.
            eligible.extend(sorted(row, reverse=True)[:limit])
        eligible.sort(reverse=True)
        return sum(eligible[:k])