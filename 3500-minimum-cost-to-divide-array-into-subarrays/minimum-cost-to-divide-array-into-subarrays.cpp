class Solution {
public:
    long long minimumCost(vector<int>& nums, vector<int>& cost, int k) {
        int n = nums.size();
        vector<long long> pn(n + 1, 0), pc(n + 1, 0);
        for (int i = 0; i < n; ++i) { pn[i + 1] = pn[i] + nums[i]; pc[i + 1] = pc[i] + cost[i]; }
        vector<long long> dp(n + 1, LLONG_MAX);
        dp[n] = 0;
        for (int i = n - 1; i >= 0; --i) {
            for (int j = i; j < n; ++j) {
                long long c = pn[j + 1] * (pc[j + 1] - pc[i]) + 1LL * k * (pc[n] - pc[i]) + dp[j + 1];
                dp[i] = min(dp[i], c);
            }
        }
        return dp[0];
    }
};