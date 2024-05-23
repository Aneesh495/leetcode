class Solution {
public:
    int minOperations(string s1, string s2, int x) {
        vector<int> d;
        for (int i = 0; i < (int)s1.size(); ++i) if (s1[i] != s2[i]) d.push_back(i);
        int m = d.size();
        if (m % 2) return -1;
        if (m == 0) return 0;
        int prev2 = 0, prev1 = x;
        for (int i = 1; i < m; ++i) {
            int cur = min(prev1 + x, prev2 + 2 * (d[i] - d[i - 1]));
            prev2 = prev1; prev1 = cur;
        }
        return prev1 / 2;
    }
};
