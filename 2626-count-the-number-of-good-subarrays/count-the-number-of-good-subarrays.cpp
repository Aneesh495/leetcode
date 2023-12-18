class Solution {
public:
    long long countGood(vector<int>& nums, int k) {
        unordered_map<int, int> cnt;
        long long pairs = 0, ans = 0;
        int l = 0;
        for (int r = 0; r < (int)nums.size(); ++r) {
            pairs += cnt[nums[r]]++;
            while (pairs >= k) pairs -= --cnt[nums[l++]];
            ans += l;
        }
        return ans;
    }
};
