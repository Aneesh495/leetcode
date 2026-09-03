class Solution {
public:
    vector<long long> earliestActivationTimes(int n, vector<vector<int>>& edges, vector<int>& requiredSignals) {
        sort(edges.begin(), edges.end());
        vector<vector<pair<int, int>>> adj(n);
        for (int i = 0; i < (int)edges.size(); ) {
            int u = edges[i][0], v = edges[i][1], d = edges[i][2];
            int j = i + 1;
            while (j < (int)edges.size() && edges[j][0] == u && edges[j][1] == v) {
                d = min(d, edges[j][2]);
                j++;
            }
            adj[u].push_back({v, d});
            i = j;
        }
        vector<long long> ans(n, -1);
        vector<int> cnt(n, 0);
        using P = pair<long long, int>;
        priority_queue<P, vector<P>, greater<P>> pq;
        ans[0] = 0;
        for (auto& [v, d] : adj[0]) pq.push({d, v});
        for (int i = 1; i < n; ++i) {
            if (requiredSignals[i] == 0) {
                ans[i] = 0;
                for (auto& [v, d] : adj[i]) pq.push({d, v});
            }
        }
        while (!pq.empty()) {
            auto [t, u] = pq.top(); pq.pop();
            if (ans[u] != -1) continue;
            cnt[u]++;
            if (cnt[u] >= requiredSignals[u]) {
                ans[u] = t;
                for (auto& [v, d] : adj[u]) {
                    if (ans[v] == -1) pq.push({t + d, v});
                }
            }
        }
        return ans;
    }
};