class Solution {
public:
    int maxValue(vector<int>& nums, int k) {
        int n = nums.size();
        vector<vector<bitset<128>>> pref(n + 1, vector<bitset<128>>(k + 1));
        vector<vector<bitset<128>>> suff(n + 1, vector<bitset<128>>(k + 1));
        pref[0][0].set(0);
        for (int i = 1; i <= n; ++i) {
            pref[i] = pref[i - 1];
            for (int count = 1; count <= min(k, i); ++count) {
                for (int mask = 0; mask < 128; ++mask) {
                    if (pref[i - 1][count - 1].test(mask))
                        pref[i][count].set(mask | nums[i - 1]);
                }
            }
        }
        suff[n][0].set(0);
        for (int i = n - 1; i >= 0; --i) {
            suff[i] = suff[i + 1];
            for (int count = 1; count <= min(k, n - i); ++count) {
                for (int mask = 0; mask < 128; ++mask) {
                    if (suff[i + 1][count - 1].test(mask))
                        suff[i][count].set(mask | nums[i]);
                }
            }
        }
        int answer = 0;
        for (int split = k; split <= n - k; ++split) {
            for (int left = 0; left < 128; ++left) {
                if (!pref[split][k].test(left)) continue;
                for (int right = 0; right < 128; ++right) {
                    if (suff[split][k].test(right))
                        answer = max(answer, left ^ right);
                }
            }
        }
        return answer;
    }
};