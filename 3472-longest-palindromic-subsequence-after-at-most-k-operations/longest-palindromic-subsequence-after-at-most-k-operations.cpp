class Solution {
public:
    int longestPalindromicSubsequence(string s, int k) {
        int n = s.size();
        vector<vector<vector<int>>> dp(n, vector<vector<int>>(n, vector<int>(k + 1, 0)));
        for (int i = 0; i < n; ++i) fill(dp[i][i].begin(), dp[i][i].end(), 1);
        for (int len = 2; len <= n; ++len) {
            for (int l = 0; l + len - 1 < n; ++l) {
                int r = l + len - 1;
                int diff = abs(s[l] - s[r]);
                int cost = min(diff, 26 - diff);
                for (int rem = 0; rem <= k; ++rem) {
                    int res = max(dp[l + 1][r][rem], dp[l][r - 1][rem]);
                    if (rem >= cost) res = max(res, 2 + (l + 1 <= r - 1 ? dp[l + 1][r - 1][rem - cost] : 0));
                    dp[l][r][rem] = res;
                }
            }
        }
        return dp[0][n - 1][k];
    }
};