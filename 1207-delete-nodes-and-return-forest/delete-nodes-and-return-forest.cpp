
class Solution {
public:
    vector<TreeNode*> delNodes(TreeNode* root, vector<int>& to_delete) {
        unordered_set<int> del(to_delete.begin(), to_delete.end());
        vector<TreeNode*> res;
        helper(root, true, del, res);
        return res;
    }
private:
    TreeNode* helper(TreeNode* node, bool isRoot, unordered_set<int>& del, vector<TreeNode*>& res) {
        if (!node) return nullptr;
        bool deleted = del.count(node->val);
        if (isRoot && !deleted) res.push_back(node);
        node->left = helper(node->left, deleted, del, res);
        node->right = helper(node->right, deleted, del, res);
        return deleted ? nullptr : node;
    }
};
