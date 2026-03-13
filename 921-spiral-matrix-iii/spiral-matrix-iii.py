
class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        res = []
        r, c = rStart, cStart
        total = rows * cols
        if 0 <= r < rows and 0 <= c < cols:
            res.append([r, c])
        steps = 1
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while len(res) < total:
            for d in range(4):
                dr, dc = dirs[d]
                for _ in range(steps):
                    r += dr
                    c += dc
                    if 0 <= r < rows and 0 <= c < cols:
                        res.append([r, c])
                        if len(res) == total:
                            return res
                if d % 2 == 1:
                    steps += 1
        return res
