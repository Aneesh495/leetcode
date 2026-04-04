
class Solution {
public:
    vector<int> pathInZigZagTree(int label) {
        vector<int> res;
        int level = 0, val = label;
        while (val > 0) {
            val >>= 1;
            level++;
        }
        while (label > 0) {
            res.push_back(label);
            int start = 1 << (level - 1);
            int end = (1 << level) - 1;
            label = (start + end - label) / 2;
            level--;
        }
        reverse(res.begin(), res.end());
        return res;
    }
};
