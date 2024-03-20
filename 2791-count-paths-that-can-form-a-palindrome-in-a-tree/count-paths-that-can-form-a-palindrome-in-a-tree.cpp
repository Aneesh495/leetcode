class Solution {
public:
    long long countPalindromePaths(vector<int>& parent, string s) {
        int n = parent.size();
        vector<vector<pair<int, int>>> g(n);
        for (int i = 1; i < n; ++i) g[parent[i]].push_back({i, 1 << (s[i] - 'a')});
        unordered_map<int, int> cnt;
        cnt[0] = 1;
        long long ans = 0;
        auto dfs = [&](auto& self, int u, int mask) -> void {
            for (auto [v, bit] : g[u]) {
                int nm = mask ^ bit;
                ans += cnt[nm];
                for (int b = 0; b < 26; ++b) {
                    auto it = cnt.find(nm ^ (1 << b));
                    if (it != cnt.end()) ans += it->second;
                }
                cnt[nm]++;
                self(self, v, nm);
            }
        };
        dfs(dfs, 0, 0);
        return ans;
    }
};
