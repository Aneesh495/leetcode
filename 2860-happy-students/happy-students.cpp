class Solution {
public:
    int countWays(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int n = nums.size(), ans = (nums[0] > 0 ? 1 : 0);
        for (int i = 1; i < n; ++i) {
            if (nums[i - 1] < i && i < nums[i]) ans++;
        }
        if (nums.back() < n) ans++;
        return ans;
    }
};
