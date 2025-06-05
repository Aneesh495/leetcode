class Solution {
public:
    vector<int> longestCommonPrefix(vector<string>& words, int k) {
        int n = words.size();
        vector<int> ans(n, 0);
        if (n - 1 < k) return ans;
        vector<int> idx(n);
        iota(idx.begin(), idx.end(), 0);
        sort(idx.begin(), idx.end(), [&](int a, int b) { return words[a] < words[b]; });
        auto lcp = [&](int a, int b) {
            int len = min(words[a].size(), words[b].size()), res = 0;
            while (res < len && words[a][res] == words[b][res]) ++res;
            return res;
        };
        int best1 = 0, bestL = -1, second1 = 0;
        for (int i = 0; i + k - 1 < n; ++i) {
            int v = lcp(idx[i], idx[i + k - 1]);
            if (v >= best1) { second1 = best1; best1 = v; bestL = i; }
            else if (v > second1) second1 = v;
        }
        int best2 = 0;
        for (int i = 0; i + k < n; ++i) {
            best2 = max(best2, lcp(idx[i], idx[i + k]));
        }
        vector<int> pos(n);
        for (int i = 0; i < n; ++i) pos[idx[i]] = i;
        for (int i = 0; i < n; ++i) {
            int p = pos[i];
            if (p >= bestL && p <= bestL + k - 1) ans[i] = max(second1, best2);
            else ans[i] = best1;
        }
        return ans;
    }
};