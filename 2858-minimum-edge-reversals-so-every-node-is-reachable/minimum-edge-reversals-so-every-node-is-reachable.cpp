class Solution {
public:
    vector<int> minEdgeReversals(int n, vector<vector<int>>& edges) {
        vector<vector<pair<int, int>>> g(n);
        for (const auto& e : edges) { g[e[0]].push_back({e[1], 0}); g[e[1]].push_back({e[0], 1}); }
        vector<int> ans(n, 0);
        auto dfs1 = [&](auto& self, int u, int p) -> int {
            int res = 0;
            for (auto [v, w] : g[u]) if (v != p) res += w + self(self, v, u);
            return res;
        };
        ans[0] = dfs1(dfs1, 0, -1);
        auto dfs2 = [&](auto& self, int u, int p) -> void {
            for (auto [v, w] : g[u]) {
                if (v == p) continue;
                ans[v] = ans[u] + (w == 0 ? 1 : -1);
                self(self, v, u);
            }
        };
        dfs2(dfs2, 0, -1);
        return ans;
    }
};
