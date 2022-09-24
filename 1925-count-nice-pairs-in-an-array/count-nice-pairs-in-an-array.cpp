class Solution {
public:
    int countNicePairs(vector<int>& nums) {
        constexpr int MOD = 1'000'000'007;
        unordered_map<int, int> seen;
        long long answer = 0;
        for (int x : nums) {
            int reversed = 0, value = x;
            while (value > 0) {
                reversed = reversed * 10 + value % 10;
                value /= 10;
            }
            int key = x - reversed;
            answer = (answer + seen[key]) % MOD;
            ++seen[key];
        }
        return static_cast<int>(answer);
    }
};