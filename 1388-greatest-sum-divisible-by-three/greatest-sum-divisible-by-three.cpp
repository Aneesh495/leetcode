class Solution {
public:
    int maxSumDivThree(vector<int>& nums) {
        vector<int> dp = {0, -1000000000, -1000000000};
        for (int x : nums) {
            vector<int> next = dp;
            for (int r = 0; r < 3; ++r)
                next[(r + x) % 3] = max(next[(r + x) % 3], dp[r] + x);
            dp = next;
        }
        return dp[0];
    }
};