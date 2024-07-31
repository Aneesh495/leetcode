
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        cur = root
        while cur:
            if cur.val == val:
                return cur
            cur = cur.left if val < cur.val else cur.right
        return None
