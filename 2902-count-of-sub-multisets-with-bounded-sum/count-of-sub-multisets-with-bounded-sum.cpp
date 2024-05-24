class Solution {
public:
    int countSubMultisets(vector<int>& nums, int l, int r) {
        const int MOD = 1e9 + 7;
        unordered_map<int, int> cnt;
        for (int x : nums) cnt[x]++;
        vector<long long> dp(r + 1, 0);
        dp[0] = cnt[0] + 1;
        cnt.erase(0);
        for (auto [x, c] : cnt) {
            vector<long long> ndp = dp;
            for (int s = x; s <= r; ++s) ndp[s] = (ndp[s] + ndp[s - x]) % MOD;
            for (int s = r; s >= (c + 1) * x; --s) ndp[s] = (ndp[s] - ndp[s - (c + 1) * x] + MOD) % MOD;
            dp = move(ndp);
        }
        long long ans = 0;
        for (int s = l; s <= r; ++s) ans = (ans + dp[s]) % MOD;
        return ans;
    }
};
