class Solution {
public:
    int countCells(vector<vector<char>>& grid, string pattern) {
        int m = grid.size(), n = grid[0].size(), p = pattern.size();
        vector<int> lps(p, 0);
        for (int i = 1, j = 0; i < p; ++i) {
            while (j > 0 && pattern[i] != pattern[j]) j = lps[j - 1];
            if (pattern[i] == pattern[j]) ++j;
            lps[i] = j;
        }
        auto kmp = [&](const string& s) {
            int N = s.size();
            vector<int> diff(N + 1, 0);
            for (int i = 0, j = 0; i < N; ++i) {
                while (j > 0 && s[i] != pattern[j]) j = lps[j - 1];
                if (s[i] == pattern[j]) ++j;
                if (j == p) { diff[i - p + 1]++; diff[i + 1]--; j = lps[j - 1]; }
            }
            vector<bool> cov(N, false);
            int cur = 0;
            for (int i = 0; i < N; ++i) { cur += diff[i]; cov[i] = cur > 0; }
            return cov;
        };
        string h, v;
        h.reserve(m * n); v.reserve(m * n);
        for (int i = 0; i < m; ++i) for (int j = 0; j < n; ++j) h.push_back(grid[i][j]);
        for (int j = 0; j < n; ++j) for (int i = 0; i < m; ++i) v.push_back(grid[i][j]);
        auto ch = kmp(h), cv = kmp(v);
        int ans = 0;
        for (int i = 0; i < m; ++i) for (int j = 0; j < n; ++j) {
            if (ch[i * n + j] && cv[j * m + i]) ++ans;
        }
        return ans;
    }
};