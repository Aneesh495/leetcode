
class Solution {
public:
    TreeNode* lcaDeepestLeaves(TreeNode* root) {
        return dfs(root).second;
    }
private:
    pair<int, TreeNode*> dfs(TreeNode* node) {
        if (!node) return {0, nullptr};
        auto L = dfs(node->left), R = dfs(node->right);
        if (L.first == R.first) return {L.first + 1, node};
        return L.first > R.first ? make_pair(L.first + 1, L.second) : make_pair(R.first + 1, R.second);
    }
};
