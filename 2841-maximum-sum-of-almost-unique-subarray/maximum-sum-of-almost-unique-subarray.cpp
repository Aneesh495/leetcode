class Solution {
public:
    long long maxSum(vector<int>& nums, int m, int k) {
        unordered_map<int, int> cnt;
        long long sum = 0, ans = 0;
        for (int i = 0; i < (int)nums.size(); ++i) {
            sum += nums[i];
            cnt[nums[i]]++;
            if (i >= k) {
                sum -= nums[i - k];
                if (--cnt[nums[i - k]] == 0) cnt.erase(nums[i - k]);
            }
            if (i >= k - 1 && (int)cnt.size() >= m) ans = max(ans, sum);
        }
        return ans;
    }
};
