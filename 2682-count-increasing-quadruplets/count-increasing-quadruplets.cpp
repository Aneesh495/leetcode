class Solution {
public:
    long long countQuadruplets(vector<int>& nums) {
        int n = nums.size();
        vector<long long> dp(n, 0);
        long long ans = 0;
        for (int j = 0; j < n; ++j) {
            int prev_small = 0;
            for (int i = 0; i < j; ++i) {
                if (nums[j] > nums[i]) {
                    prev_small++;
                    ans += dp[i];
                } else {
                    dp[i] += prev_small;
                }
            }
        }
        return ans;
    }
};
