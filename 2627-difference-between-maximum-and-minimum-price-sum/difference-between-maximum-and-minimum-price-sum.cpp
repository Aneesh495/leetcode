class Solution {
public:
    long long maxOutput(int n, vector<vector<int>>& edges, vector<int>& price) {
        vector<vector<int>> g(n);
        for (const auto& e : edges) { g[e[0]].push_back(e[1]); g[e[1]].push_back(e[0]); }
        long long ans = 0;
        auto dfs = [&](auto& self, int u, int p) -> pair<long long, long long> {
            long long withLeaf = price[u], noLeaf = 0;
            for (int v : g[u]) {
                if (v == p) continue;
                auto [wl, nl] = self(self, v, u);
                ans = max({ans, withLeaf + nl, noLeaf + wl});
                withLeaf = max(withLeaf, wl + price[u]);
                noLeaf = max(noLeaf, nl + price[u]);
            }
            return {withLeaf, noLeaf};
        };
        dfs(dfs, 0, -1);
        return ans;
    }
};
