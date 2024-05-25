class Solution {
public:
    vector<vector<int>> constructProductMatrix(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size(), MOD = 12345;
        vector<vector<int>> ans(m, vector<int>(n, 1));
        long long p = 1;
        for (int i = 0; i < m; ++i)
            for (int j = 0; j < n; ++j) { ans[i][j] = p; p = p * grid[i][j] % MOD; }
        p = 1;
        for (int i = m - 1; i >= 0; --i)
            for (int j = n - 1; j >= 0; --j) { ans[i][j] = ans[i][j] * p % MOD; p = p * grid[i][j] % MOD; }
        return ans;
    }
};
