class Solution {
public:
    long long getMaxFunctionValue(vector<int>& receiver, long long k) {
        int n = receiver.size(), LOG = 35;
        vector<vector<int>> up(LOG, vector<int>(n));
        vector<vector<long long>> sum(LOG, vector<long long>(n));
        for (int i = 0; i < n; ++i) { up[0][i] = receiver[i]; sum[0][i] = receiver[i]; }
        for (int j = 1; j < LOG; ++j) {
            for (int i = 0; i < n; ++i) {
                up[j][i] = up[j - 1][up[j - 1][i]];
                sum[j][i] = sum[j - 1][i] + sum[j - 1][up[j - 1][i]];
            }
        }
        long long ans = 0;
        for (int i = 0; i < n; ++i) {
            long long cur = i;
            int u = i;
            for (int j = 0; j < LOG; ++j) {
                if (k & (1LL << j)) { cur += sum[j][u]; u = up[j][u]; }
            }
            ans = max(ans, cur);
        }
        return ans;
    }
};
