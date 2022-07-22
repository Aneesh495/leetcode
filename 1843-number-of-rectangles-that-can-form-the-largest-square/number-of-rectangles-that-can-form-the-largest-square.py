class Solution:
    def countGoodRectangles(self, rectangles):
        sides=[min(r) for r in rectangles]
        return sides.count(max(sides))