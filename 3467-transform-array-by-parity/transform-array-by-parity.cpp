class Solution {
public:
    vector<int> transformArray(vector<int>& nums) {
        int ev = 0;
        for (int x : nums) if ((x & 1) == 0) ++ev;
        vector<int> ans(nums.size(), 1);
        fill(ans.begin(), ans.begin() + ev, 0);
        return ans;
    }
};