class Solution {
public:
    long long minCost(vector<int>& nums) {
        int n = nums.size();
        long long ans = LLONG_MAX;
        for (int i = 0; i < n; ) {
            int j = i;
            while (j < n && nums[j] == nums[i]) j++;
            int l = i, r = j - 1;
            if (l == 0 && r == n - 1) return 0;
            if (l == 0) {
                if (r > 0) ans = min(ans, 1LL * (n - 1 - r) * nums[i]);
            } else if (r == n - 1) {
                if (l < n - 1) ans = min(ans, 1LL * l * nums[i]);
            } else {
                ans = min(ans, 1LL * (l + n - 1 - r) * nums[i]);
            }
            i = j;
        }
        return ans;
    }
};