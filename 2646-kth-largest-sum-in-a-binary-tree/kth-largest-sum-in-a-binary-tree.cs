public class Solution {
    public long KthLargestLevelSum(TreeNode root, int k) {
        var queue = new Queue<TreeNode>();
        queue.Enqueue(root);
        var sums = new List<long>();
        while (queue.Count > 0) {
            int size = queue.Count;
            long sum = 0;
            for (int i = 0; i < size; i++) {
                TreeNode node = queue.Dequeue();
                sum += node.val;
                if (node.left != null) queue.Enqueue(node.left);
                if (node.right != null) queue.Enqueue(node.right);
            }
            sums.Add(sum);
        }
        if (k > sums.Count) return -1;
        sums.Sort((a, b) => b.CompareTo(a));
        return sums[k - 1];
    }
}