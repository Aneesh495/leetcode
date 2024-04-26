class Solution {
public:
    int minLengthAfterRemovals(vector<int>& nums) {
        int n = nums.size(), mx = 0;
        for (int i = 0; i < n; ) {
            int j = i;
            while (j < n && nums[j] == nums[i]) j++;
            mx = max(mx, j - i);
            i = j;
        }
        return mx * 2 > n ? 2 * mx - n : n % 2;
    }
};
