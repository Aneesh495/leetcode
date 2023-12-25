class Solution {
public:
    int minCost(vector<int>& nums, int k) {
        int n = nums.size();
        vector<long long> dp(n + 1, 1e18);
        dp[0] = 0;
        for (int i = 1; i <= n; ++i) {
            unordered_map<int, int> cnt;
            long long trimmed = 0;
            for (int j = i - 1; j >= 0; --j) {
                int c = ++cnt[nums[j]];
                if (c == 2) trimmed += 2;
                else if (c > 2) trimmed += 1;
                dp[i] = min(dp[i], dp[j] + k + trimmed);
            }
        }
        return dp[n];
    }
};
