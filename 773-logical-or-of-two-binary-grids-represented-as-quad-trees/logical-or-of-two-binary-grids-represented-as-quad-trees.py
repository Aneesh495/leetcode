
# Definition for a QuadTree node.
# class Node:
#     def __init__(self, val, isLeaf, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
#         self.val = val
#         self.isLeaf = isLeaf
#         self.topLeft = topLeft
#         self.topRight = topRight
#         self.bottomLeft = bottomLeft
#         self.bottomRight = bottomRight

class Solution:
    def intersect(self, q1: 'Node', q2: 'Node') -> 'Node':
        if q1.isLeaf:
            return Node(True, True) if q1.val else q2
        if q2.isLeaf:
            return Node(True, True) if q2.val else q1

        tl = self.intersect(q1.topLeft, q2.topLeft)
        tr = self.intersect(q1.topRight, q2.topRight)
        bl = self.intersect(q1.bottomLeft, q2.bottomLeft)
        br = self.intersect(q1.bottomRight, q2.bottomRight)

        if tl.isLeaf and tr.isLeaf and bl.isLeaf and br.isLeaf and \
           tl.val == tr.val == bl.val == br.val:
            return Node(tl.val, True)
        return Node(False, False, tl, tr, bl, br)
