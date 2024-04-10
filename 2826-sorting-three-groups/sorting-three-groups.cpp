class Solution {
public:
    int minimumOperations(vector<int>& nums) {
        int dp[4] = {};
        for (int x : nums) {
            dp[x]++;
            dp[2] = max(dp[2], dp[1]);
            dp[3] = max(dp[3], dp[2]);
        }
        return nums.size() - dp[3];
    }
};
