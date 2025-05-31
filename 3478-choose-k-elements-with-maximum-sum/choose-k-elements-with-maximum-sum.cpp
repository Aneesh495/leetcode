class Solution {
public:
    vector<long long> findMaxSum(vector<int>& nums1, vector<int>& nums2, int k) {
        int n = nums1.size();
        vector<int> idx(n);
        iota(idx.begin(), idx.end(), 0);
        sort(idx.begin(), idx.end(), [&](int a, int b) { return nums1[a] < nums1[b]; });
        vector<long long> ans(n, 0);
        priority_queue<int, vector<int>, greater<int>> pq;
        long long sum = 0;
        for (int i = 0; i < n; ) {
            int j = i;
            while (j < n && nums1[idx[j]] == nums1[idx[i]]) ++j;
            for (int p = i; p < j; ++p) ans[idx[p]] = sum;
            for (int p = i; p < j; ++p) {
                int v = nums2[idx[p]];
                pq.push(v); sum += v;
                if ((int)pq.size() > k) { sum -= pq.top(); pq.pop(); }
            }
            i = j;
        }
        return ans;
    }
};