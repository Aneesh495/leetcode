class Solution {
public:
    int maxDifference(string s, int k) {
        int n = s.size();
        array<vector<int>, 5> pref;
        for (int digit = 0; digit < 5; ++digit) {
            pref[digit].assign(n + 1, 0);
            for (int i = 0; i < n; ++i) {
                pref[digit][i + 1] = pref[digit][i] + (s[i] == '0' + digit);
            }
        }
        constexpr int infinity = 1000000000;
        int best = -infinity;
        for (int a = 0; a < 5; ++a) {
            for (int b = 0; b < 5; ++b) {
                if (a == b) continue;
                int minDifference[4] = {infinity, infinity, infinity, infinity};
                int left = 0;
                for (int right = k; right <= n; ++right) {
                    // Only record starts that already give enough length and two copies of b.
                    while (right - left >= k && pref[b][right] - pref[b][left] >= 2) {
                        int state = 2 * (pref[a][left] & 1) + (pref[b][left] & 1);
                        minDifference[state] = min(minDifference[state], pref[a][left] - pref[b][left]);
                        ++left;
                    }
                    // For an odd count of a, flip its parity. For even b, preserve parity.
                    int need = 2 * ((pref[a][right] & 1) ^ 1) + (pref[b][right] & 1);
                    if (minDifference[need] != infinity) {
                        best = max(best, pref[a][right] - pref[b][right] - minDifference[need]);
                    }
                }
            }
        }
        return best;
    }
};