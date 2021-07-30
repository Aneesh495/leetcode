class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        queen_set = set((r, c) for r, c in queens)
        res = []

        directions = [
            (-1, 0), (1, 0), (0, -1), (0, 1),
            (-1, -1), (-1, 1), (1, -1), (1, 1)
        ]

        for dr, dc in directions:
            r, c = king
            while 0 <= r + dr < 8 and 0 <= c + dc < 8:
                r += dr
                c += dc
                if (r, c) in queen_set:
                    res.append([r, c])
                    break

        return res
