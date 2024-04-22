class Solution {
public:
    vector<int> minOperationsQueries(int n, vector<vector<int>>& edges, vector<vector<int>>& queries) {
        vector<vector<pair<int, int>>> g(n);
        for (const auto& e : edges) { g[e[0]].push_back({e[1], e[2]}); g[e[1]].push_back({e[0], e[2]}); }
        int LOG = 15;
        vector<vector<int>> up(LOG, vector<int>(n, 0)), cnt(n, vector<int>(27, 0));
        vector<int> depth(n, 0);
        auto dfs = [&](auto& self, int u, int p) -> void {
            up[0][u] = p;
            for (int j = 1; j < LOG; ++j) up[j][u] = up[j - 1][up[j - 1][u]];
            for (auto [v, w] : g[u]) {
                if (v == p) continue;
                depth[v] = depth[u] + 1;
                cnt[v] = cnt[u];
                cnt[v][w]++;
                self(self, v, u);
            }
        };
        dfs(dfs, 0, 0);
        auto lca = [&](int a, int b) {
            if (depth[a] < depth[b]) swap(a, b);
            int diff = depth[a] - depth[b];
            for (int j = 0; j < LOG; ++j) if (diff & (1 << j)) a = up[j][a];
            if (a == b) return a;
            for (int j = LOG - 1; j >= 0; --j) {
                if (up[j][a] != up[j][b]) { a = up[j][a]; b = up[j][b]; }
            }
            return up[0][a];
        };
        vector<int> ans;
        for (const auto& q : queries) {
            int u = q[0], v = q[1], l = lca(u, v);
            int tot = depth[u] + depth[v] - 2 * depth[l], mx = 0;
            for (int w = 1; w <= 26; ++w) mx = max(mx, cnt[u][w] + cnt[v][w] - 2 * cnt[l][w]);
            ans.push_back(tot - mx);
        }
        return ans;
    }
};
