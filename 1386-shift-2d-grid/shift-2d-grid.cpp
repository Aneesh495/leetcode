class Solution {
public:
    vector<vector<int>> shiftGrid(vector<vector<int>>& grid, int k) {
        int m = grid.size(), n = grid[0].size();
        vector<vector<int>> ans(m, vector<int>(n));
        for (int i = 0; i < m * n; ++i) {
            int j = (i + k) % (m * n);
            ans[j / n][j % n] = grid[i / n][i % n];
        }
        return ans;
    }
};