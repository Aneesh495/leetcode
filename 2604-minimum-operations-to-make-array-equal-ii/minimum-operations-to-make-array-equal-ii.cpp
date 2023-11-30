class Solution {
public:
    long long minOperations(vector<int>& nums1, vector<int>& nums2, int k) {
        if (k == 0) return nums1 == nums2 ? 0 : -1;
        long long pos = 0, neg = 0;
        for (int i = 0; i < (int)nums1.size(); ++i) {
            long long d = nums1[i] - nums2[i];
            if (d % k != 0) return -1;
            if (d > 0) pos += d / k;
            else neg += -d / k;
        }
        return pos == neg ? pos : -1;
    }
};
