
class Solution {
    int leftCount = 0, rightCount = 0;
    
    public boolean btreeGameWinningMove(TreeNode root, int n, int x) {
        count(root, x);
        int parent = n - leftCount - rightCount - 1;
        int half = n / 2;
        return leftCount > half || rightCount > half || parent > half;
    }

    private int count(TreeNode node, int x) {
        if (node == null) return 0;
        int left = count(node.left, x);
        int right = count(node.right, x);
        if (node.val == x) {
            leftCount = left;
            rightCount = right;
        }
        return left + right + 1;
    }
}
