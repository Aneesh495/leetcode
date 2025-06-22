class Solution {
public:
    int minimumPairRemoval(vector<int>& nums) {
        int ans = 0;
        while (!is_sorted(nums.begin(), nums.end())) {
            int idx = 0, best = nums[0] + nums[1];
            for (int i = 1; i + 1 < (int)nums.size(); ++i) {
                if (nums[i] + nums[i + 1] < best) { best = nums[i] + nums[i + 1]; idx = i; }
            }
            nums[idx] = best;
            nums.erase(nums.begin() + idx + 1);
            ++ans;
        }
        return ans;
    }
};