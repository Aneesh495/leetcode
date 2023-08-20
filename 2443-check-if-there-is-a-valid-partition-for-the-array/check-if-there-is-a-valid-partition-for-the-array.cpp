class Solution {
public:
    bool validPartition(vector<int>& nums) {
        int n = nums.size();
        vector<char> dp(n + 1, false);
        dp[0] = true;
        for (int i = 2; i <= n; ++i) {
            if (dp[i - 2] && nums[i - 1] == nums[i - 2]) dp[i] = true;
            if (i >= 3 && dp[i - 3]) {
                bool allEqual = nums[i - 1] == nums[i - 2] && nums[i - 2] == nums[i - 3];
                bool consecutive = nums[i - 3] + 1 == nums[i - 2] && nums[i - 2] + 1 == nums[i - 1];
                if (allEqual || consecutive) dp[i] = true;
            }
        }
        return dp[n];
    }
};