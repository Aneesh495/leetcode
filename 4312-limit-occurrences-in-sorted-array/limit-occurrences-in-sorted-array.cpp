class Solution {
public:
    vector<int> limitOccurrences(vector<int>& nums, int k) {
        int written = 0;
        for (int value : nums) {
            // A matching value k places back means the quota is already filled.
            if (written < k || nums[written - k] != value) nums[written++] = value;
        }
        nums.resize(written);
        return nums;
    }
};