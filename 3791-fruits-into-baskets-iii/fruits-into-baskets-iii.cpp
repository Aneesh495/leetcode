class Solution {
public:
    int numOfUnplacedFruits(vector<int>& fruits, vector<int>& baskets) {
        int n = baskets.size();
        vector<int> tree(4 * n);
        function<void(int, int, int)> build = [&](int node, int left, int right) {
            if (left == right) {
                tree[node] = baskets[left];
                return;
            }
            int mid = (left + right) / 2;
            build(node * 2, left, mid);
            build(node * 2 + 1, mid + 1, right);
            tree[node] = max(tree[node * 2], tree[node * 2 + 1]);
        };
        function<bool(int, int, int, int)> place = [&](int node, int left, int right, int need) {
            if (tree[node] < need) return false;
            if (left == right) {
                tree[node] = 0;
                return true;
            }
            int mid = (left + right) / 2;
            bool placed;
            if (tree[node * 2] >= need) placed = place(node * 2, left, mid, need);
            else placed = place(node * 2 + 1, mid + 1, right, need);
            tree[node] = max(tree[node * 2], tree[node * 2 + 1]);
            return placed;
        };
        build(1, 0, n - 1);
        int unplaced = 0;
        for (int fruit : fruits) if (!place(1, 0, n - 1, fruit)) ++unplaced;
        return unplaced;
    }
};