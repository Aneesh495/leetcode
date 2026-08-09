class Solution:
    def lastVisitedCell(self, grid: list[list[str]]) -> list[int]:
        rows, cols = len(grid), len(grid[0])
        move = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}
        seen = bytearray(rows * cols)
        row, col = 0, 0
        seen[0] = 1
        while True:
            dr, dc = move[grid[row][col]]
            nr, nc = row + dr, col + dc
            if not (0 <= nr < rows and 0 <= nc < cols) or seen[nr * cols + nc]:
                return [row, col]
            seen[nr * cols + nc] = 1
            row, col = nr, nc