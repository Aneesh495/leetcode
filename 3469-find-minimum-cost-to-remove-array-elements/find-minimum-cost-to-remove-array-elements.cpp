class Solution {
public:
    int minCost(vector<int>& nums) {
        int n = nums.size();
        vector<vector<int>> memo(n + 1, vector<int>(n + 1, -1));
        auto dfs = [&](auto& self, int i, int prev) -> int {
            if (i == n) return nums[prev];
            if (i == n - 1) return max(nums[prev], nums[i]);
            if (memo[i][prev] != -1) return memo[i][prev];
            int a = max(nums[i], nums[i + 1]) + self(self, i + 2, prev);
            int b = max(nums[prev], nums[i + 1]) + self(self, i + 2, i);
            int c = max(nums[prev], nums[i]) + self(self, i + 2, i + 1);
            return memo[i][prev] = min({a, b, c});
        };
        return dfs(dfs, 1, 0);
    }
};