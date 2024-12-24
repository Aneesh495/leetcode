class Solution {
public:
    int numberOfGoodPartitions(vector<int>& nums) {
        constexpr int mod = 1000000007;
        unordered_map<int, int> last;
        for (int i = 0; i < nums.size(); ++i) last[nums[i]] = i;
        int right = 0;
        int ways = 1;
        for (int i = 0; i < nums.size(); ++i) {
            right = max(right, last[nums[i]]);
            // Each completed block boundary independently permits a cut.
            if (i == right && i + 1 < nums.size()) ways = ways * 2 % mod;
        }
        return ways;
    }
};