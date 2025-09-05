class Solution {
public:
    long long maximumMedianSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int n = nums.size();
        long long ans = 0;
        for (int i = n - 2, cnt = 0; cnt < n / 3; i -= 2, ++cnt) ans += nums[i];
        return ans;
    }
};