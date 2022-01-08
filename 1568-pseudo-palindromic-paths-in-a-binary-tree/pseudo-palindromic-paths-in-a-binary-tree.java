class Solution {
    public int pseudoPalindromicPaths(TreeNode root) {
        Deque<TreeNode> nodes = new ArrayDeque<>();
        Deque<Integer> masks = new ArrayDeque<>();
        nodes.push(root); masks.push(0);
        int answer=0;
        while (!nodes.isEmpty()) {
            TreeNode node=nodes.pop(); int mask=masks.pop() ^ (1 << node.val);
            if (node.left==null && node.right==null && (mask & (mask-1))==0) answer++;
            if (node.left!=null) { nodes.push(node.left); masks.push(mask); }
            if (node.right!=null) { nodes.push(node.right); masks.push(mask); }
        }
        return answer;
    }
}