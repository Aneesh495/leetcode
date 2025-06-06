class Solution {
public:
    int maxSum(vector<int>& nums) {
        int mx = *max_element(nums.begin(), nums.end());
        if (mx <= 0) return mx;
        unordered_set<int> s;
        int ans = 0;
        for (int x : nums) if (x > 0 && s.insert(x).second) ans += x;
        return ans;
    }
};