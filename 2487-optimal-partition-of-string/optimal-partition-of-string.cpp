class Solution {
public:
    int partitionString(string s) {
        int parts = 1, mask = 0;
        for (char c : s) {
            int bit = 1 << (c - 'a');
            if (mask & bit) {
                ++parts;
                mask = 0;
            }
            mask |= bit;
        }
        return parts;
    }
};