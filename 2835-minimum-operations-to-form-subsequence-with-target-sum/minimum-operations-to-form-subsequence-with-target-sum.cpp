class Solution {
public:
    int minOperations(vector<int>& nums, int target) {
        long long tot = accumulate(nums.begin(), nums.end(), 0LL);
        if (tot < target) return -1;
        int cnt[32] = {};
        for (int x : nums) cnt[__builtin_ctz(x)]++;
        int ans = 0;
        for (int i = 0; i < 31; ++i) {
            if (target & (1 << i)) {
                if (cnt[i] > 0) cnt[i]--;
                else {
                    int j = i + 1;
                    while (cnt[j] == 0) j++;
                    cnt[j]--;
                    for (int k = i + 1; k < j; ++k) cnt[k]++;
                    ans += j - i;
                }
            }
            cnt[i + 1] += cnt[i] / 2;
        }
        return ans;
    }
};
