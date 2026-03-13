
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        row = [0.0] * (query_row + 2)
        row[0] = float(poured)
        for r in range(query_row):
            next_row = [0.0] * (query_row + 2)
            for c in range(r + 1):
                overflow = max(0.0, (row[c] - 1.0) / 2.0)
                if overflow > 0:
                    next_row[c] += overflow
                    next_row[c + 1] += overflow
            row = next_row
        return min(1.0, row[query_glass])
