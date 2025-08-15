class Solution {
public:
    vector<int> longestCommonPrefix(vector<string>& words) {
        int n = words.size();
        vector<int> ans(n, 0);
        if (n <= 2) return ans;
        auto lcp = [&](int i, int j) {
            int len = min(words[i].size(), words[j].size()), r = 0;
            while (r < len && words[i][r] == words[j][r]) ++r;
            return r;
        };
        vector<int> adj(n - 1), pref(n, 0), suff(n, 0);
        for (int i = 0; i + 1 < n; ++i) adj[i] = lcp(i, i + 1);
        for (int i = 0; i + 1 < n; ++i) pref[i + 1] = max(pref[i], adj[i]);
        for (int i = n - 2; i >= 0; --i) suff[i] = max(suff[i + 1], adj[i]);
        for (int i = 0; i < n; ++i) {
            int res = 0;
            if (i >= 2) res = max(res, pref[i - 1]);
            if (i + 2 < n) res = max(res, suff[i + 1]);
            if (i > 0 && i + 1 < n) res = max(res, lcp(i - 1, i + 1));
            ans[i] = res;
        }
        return ans;
    }
};