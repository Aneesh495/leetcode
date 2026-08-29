class Solution {
public:
    long long countConsistent(vector<int>& nums) {
        const int n = nums.size();
        array<int, 20> zeros;
        zeros.fill(n);
        vector<int> right(n, n);
        for (int i = n - 1; i >= 0; --i) {
            for (int bit = 0; bit < 20; ++bit) {
                if (nums[i] & (1 << bit)) right[i] = min(right[i], zeros[bit]);
                else zeros[bit] = i;
            }
        }

        zeros.fill(-1);
        vector<int> same(1000001, -1);
        long long total = 0;
        for (int i = 0; i < n; ++i) {
            // Count subarrays by the first occurrence of their minimum.
            int left = same[nums[i]];
            same[nums[i]] = i;
            for (int bit = 0; bit < 20; ++bit) {
                // Preserving all bits of nums[i] also ensures all other values are at least nums[i].
                if (nums[i] & (1 << bit)) left = max(left, zeros[bit]);
                else zeros[bit] = i;
            }
            total += 1LL * (i - left) * (right[i] - i);
        }
        return total;
    }
};