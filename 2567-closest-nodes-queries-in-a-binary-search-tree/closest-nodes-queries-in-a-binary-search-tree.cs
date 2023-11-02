public class Solution {
    public IList<IList<int>> ClosestNodes(TreeNode root, IList<int> queries) {
        var values = new List<int>();
        var stack = new Stack<TreeNode>();
        TreeNode current = root;
        while (current != null || stack.Count > 0) {
            while (current != null) {
                stack.Push(current);
                current = current.left;
            }
            current = stack.Pop();
            values.Add(current.val);
            current = current.right;
        }

        var answer = new List<IList<int>>(queries.Count);
        foreach (int query in queries) {
            int left = 0, right = values.Count;
            while (left < right) {
                int mid = left + (right - left) / 2;
                if (values[mid] < query) left = mid + 1;
                else right = mid;
            }
            int ceiling = left < values.Count ? values[left] : -1;
            int floor = left < values.Count && values[left] == query
                ? values[left]
                : (left > 0 ? values[left - 1] : -1);
            answer.Add(new List<int> { floor, ceiling });
        }
        return answer;
    }
}