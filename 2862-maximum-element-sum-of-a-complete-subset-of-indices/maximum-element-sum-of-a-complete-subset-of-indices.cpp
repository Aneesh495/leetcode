class Solution {
public:
    long long maximumSum(vector<int>& nums) {
        int n = nums.size();
        long long ans = 0;
        for (int k = 1; k <= n; ++k) {
            long long sum = 0;
            for (int v = 1; k * v * v <= n; ++v) sum += nums[k * v * v - 1];
            ans = max(ans, sum);
        }
        return ans;
    }
};
