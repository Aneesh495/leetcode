class Solution {
public:
    int minimumTime(vector<int>& nums1, vector<int>& nums2, int x) {
        int n = nums1.size();
        vector<pair<int, int>> a(n);
        for (int i = 0; i < n; ++i) a[i] = {nums2[i], nums1[i]};
        sort(a.begin(), a.end());
        vector<int> dp(n + 1, 0);
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j >= 1; --j) {
                dp[j] = max(dp[j], dp[j - 1] + a[i].second + j * a[i].first);
            }
        }
        int s1 = accumulate(nums1.begin(), nums1.end(), 0);
        int s2 = accumulate(nums2.begin(), nums2.end(), 0);
        for (int t = 0; t <= n; ++t) {
            if (s1 + t * s2 - dp[t] <= x) return t;
        }
        return -1;
    }
};
