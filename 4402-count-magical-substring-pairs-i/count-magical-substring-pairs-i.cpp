class Solution {
public:
    int countMagicalPairs(string s) {
        long long total = 0;
        for (int cut = 0; cut + 1 < s.size(); ++cut) {
            int leftCount[27] = {};
            unsigned mask = 0;
            for (int start = cut; start >= 0; --start) {
                mask |= 1u << (s[start] - 'a');
                ++leftCount[__builtin_popcount(mask)];
            }
            mask = 0;
            // Each right substring pairs with all left substrings having the same distinct count.
            for (int end = cut + 1; end < s.size(); ++end) {
                mask |= 1u << (s[end] - 'a');
                total += leftCount[__builtin_popcount(mask)];
            }
        }
        return total;
    }
};