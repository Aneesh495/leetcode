class Solution {
public:
    long long countInterestingSubarrays(vector<int>& nums, int modulo, int k) {
        unordered_map<int, long long> cnt;
        cnt[0] = 1;
        long long ans = 0;
        int pref = 0;
        for (int x : nums) {
            if (x % modulo == k) pref = (pref + 1) % modulo;
            ans += cnt[(pref - k + modulo) % modulo];
            cnt[pref]++;
        }
        return ans;
    }
};
