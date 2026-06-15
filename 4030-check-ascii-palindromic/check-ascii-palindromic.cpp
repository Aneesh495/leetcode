class Solution {
public:
    bool isPalindromic(string s) {
        const int bits = 8 * s.size();
        auto bitAt = [&](int position) { return (s[position / 8] >> (7 - position % 8)) & 1; };
        // Test mirrored bit positions directly, including the leading zero in every byte.
        for (int i = 0; i < bits / 2; ++i) {
            if (bitAt(i) != bitAt(bits - 1 - i)) return false;
        }
        return true;
    }
};