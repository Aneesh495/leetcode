class Solution {
public:
    int maxProfit(int n, vector<vector<int>>& edges, vector<int>& score) {
        vector<int> pre(n, 0);
        for (auto& e : edges) pre[e[1]] |= (1 << e[0]);
        vector<int> dp(1 << n, -1e9);
        dp[0] = 0;
        for (int mask = 0; mask < (1 << n); ++mask) {
            if (dp[mask] <= -1e9) continue;
            int pos = __builtin_popcount(mask) + 1;
            for (int i = 0; i < n; ++i) {
                if (!(mask & (1 << i)) && (mask & pre[i]) == pre[i]) {
                    dp[mask | (1 << i)] = max(dp[mask | (1 << i)], dp[mask] + pos * score[i]);
                }
            }
        }
        return dp[(1 << n) - 1];
    }
};