class Solution {
public:
    int findKthNumber(int n, int k) {
        long long prefix = 1;
        --k;  // The first trie node is already selected.
        while (k > 0) {
            long long subtreeSize = 0;
            // Count [lo, hi) clipped to [1, n] on each level of the trie.
            for (long long lo = prefix, hi = prefix + 1; lo <= n; lo *= 10, hi *= 10) {
                subtreeSize += min(hi, static_cast<long long>(n) + 1) - lo;
            }
            if (subtreeSize <= k) {
                k -= subtreeSize;
                ++prefix;
            } else {
                --k;
                prefix *= 10;
            }
        }
        return static_cast<int>(prefix);
    }
};