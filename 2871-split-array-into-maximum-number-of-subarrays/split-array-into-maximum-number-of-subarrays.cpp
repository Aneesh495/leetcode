class Solution {
public:
    int maxSubarrays(vector<int>& nums) {
        int ans = 0, cur = -1;
        for (int x : nums) {
            cur &= x;
            if (cur == 0) { ans++; cur = -1; }
        }
        return max(1, ans);
    }
};
