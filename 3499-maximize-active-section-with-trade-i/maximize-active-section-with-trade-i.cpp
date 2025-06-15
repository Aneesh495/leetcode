class Solution {
public:
    int maxActiveSectionsAfterTrade(string s) {
        int ones = 0, n = s.size();
        vector<int> z;
        for (int i = 0; i < n; ) {
            if (s[i] == '1') { ++ones; ++i; }
            else {
                int j = i;
                while (j < n && s[j] == '0') ++j;
                z.push_back(j - i);
                i = j;
            }
        }
        int gain = 0;
        for (size_t i = 0; i + 1 < z.size(); ++i) gain = max(gain, z[i] + z[i + 1]);
        return ones + gain;
    }
};