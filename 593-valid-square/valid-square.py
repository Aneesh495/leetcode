
class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def d2(a, b):
            dx = a[0] - b[0]
            dy = a[1] - b[1]
            return dx * dx + dy * dy

        pts = [p1, p2, p3, p4]
        dists = []
        for i in range(4):
            for j in range(i + 1, 4):
                dists.append(d2(pts[i], pts[j]))

        dists.sort()
        return dists[0] > 0 and dists[0] == dists[1] == dists[2] == dists[3] and dists[4] == dists[5] and dists[4] == 2 * dists[0]
