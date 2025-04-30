class Solution {
    public long numberOfPairs(int[] nums1, int[] nums2, int k) {
        int[] freq = new int[1_000_001];
        for (int value : nums2) ++freq[value];
        long pairs = 0;
        for (int value : nums1) {
            if (value % k != 0) continue;
            int quotient = value / k;
            for (int d = 1; d <= quotient / d; ++d) {
                if (quotient % d == 0) {
                    pairs += freq[d];
                    int other = quotient / d;
                    if (other != d) pairs += freq[other];
                }
            }
        }
        return pairs;
    }
}