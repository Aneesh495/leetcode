class Solution {
public:
    int partitionArray(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        int groups = 0, left = 0;
        for (int right = 0; right < (int)nums.size(); ++right) {
            if (nums[right] - nums[left] > k) {
                ++groups;
                left = right;
            }
        }
        return groups + 1;
    }
};