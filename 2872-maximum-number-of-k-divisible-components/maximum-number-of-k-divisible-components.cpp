class Solution {
public:
    int maxKDivisibleComponents(int n, vector<vector<int>>& edges, vector<int>& values, int k) {
        vector<vector<int>> g(n);
        for (const auto& e : edges) { g[e[0]].push_back(e[1]); g[e[1]].push_back(e[0]); }
        int ans = 0;
        auto dfs = [&](auto& self, int u, int p) -> long long {
            long long sum = values[u];
            for (int v : g[u]) if (v != p) sum += self(self, v, u);
            if (sum % k == 0) { ans++; return 0; }
            return sum;
        };
        dfs(dfs, 0, -1);
        return ans;
    }
};
