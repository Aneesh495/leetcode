class Solution {
public:
    int numWays(int steps, int arrLen) {
        const int mod = 1000000007;
        int n = min(arrLen, steps / 2 + 1);
        vector<int> dp(n), next(n);
        dp[0] = 1;
        for (int t = 0; t < steps; ++t) {
            fill(next.begin(), next.end(), 0);
            for (int i = 0; i < n; ++i) {
                long long v = dp[i];
                if (i) v += dp[i-1];
                if (i+1 < n) v += dp[i+1];
                next[i] = v % mod;
            }
            dp.swap(next);
        }
        return dp[0];
    }
};